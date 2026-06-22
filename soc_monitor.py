#!/usr/bin/env python3
"""
SOC Monitor - Simple Real-time Security Event Detection
"""

import json
import time
import re
import os
from datetime import datetime, timedelta
from collections import defaultdict

class SOCMonitor:
    def __init__(self):
        self.log_file = "security_events.log"
        self.alert_file = "alerts.log"
        self.rules = self.load_rules()
        self.event_buffer = defaultdict(list)
        self.alerts_count = 0
        
    def load_rules(self):
        try:
            with open("alert_rules.json", 'r', encoding='utf-8') as f:
                rules_data = json.load(f)
                print(f"[+] Loaded {len(rules_data['rules'])} detection rules")
                return rules_data['rules']
        except:
            print("[!] Using default rules")
            return [
                {
                    "id": "RULE-001",
                    "name": "Multiple Failed Login Attempts",
                    "pattern": "Failed password",
                    "threshold": 3,
                    "time_window": 30,
                    "severity": "HIGH"
                },
                {
                    "id": "RULE-002",
                    "name": "SQL Injection Attempt",
                    "pattern": "sql injection",
                    "threshold": 1,
                    "time_window": 10,
                    "severity": "CRITICAL"
                },
                {
                    "id": "RULE-003",
                    "name": "Malware Detection",
                    "pattern": "malware detected",
                    "threshold": 1,
                    "time_window": 10,
                    "severity": "CRITICAL"
                },
                {
                    "id": "RULE-004",
                    "name": "Brute Force Attack",
                    "pattern": "Failed password",
                    "threshold": 5,
                    "time_window": 60,
                    "severity": "CRITICAL"
                }
            ]
    
    def analyze_event(self, event_line):
        current_time = datetime.now()
        
        for rule in self.rules:
            if re.search(rule['pattern'], event_line, re.IGNORECASE):
                rule_id = rule['id']
                
                self.event_buffer[rule_id].append({
                    "timestamp": current_time,
                    "event": event_line
                })
                
                # Remove old events
                time_window = timedelta(seconds=rule['time_window'])
                self.event_buffer[rule_id] = [
                    e for e in self.event_buffer[rule_id]
                    if current_time - e['timestamp'] <= time_window
                ]
                
                # Trigger alert if threshold reached
                if len(self.event_buffer[rule_id]) >= rule['threshold']:
                    self.trigger_alert(rule, self.event_buffer[rule_id])
                    self.event_buffer[rule_id] = []
    
    def trigger_alert(self, rule, events):
        alert = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "rule_id": rule['id'],
            "rule_name": rule['name'],
            "severity": rule['severity'],
            "matched_count": len(events),
            "sample_events": [e['event'] for e in events[:3]]
        }
        
        # Save alert
        with open(self.alert_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(alert) + '\n')
        
        self.alerts_count += 1
        
        # Display alert
        severity_symbol = {
            "CRITICAL": "🔴",
            "HIGH": "🟡", 
            "MEDIUM": "🟠",
            "LOW": "🟢"
        }
        
        symbol = severity_symbol.get(rule['severity'], "⚠️")
        print(f"\n{symbol} ALERT #{self.alerts_count}: {rule['severity']} - {rule['name']}")
        print(f"   Time: {alert['timestamp']}")
        print(f"   Events: {len(events)} matches")
    
    def start_monitoring(self):
        print("="*50)
        print("  SOC MONITOR - Real-time Threat Detection")
        print("="*50)
        print(f"[*] Monitoring: {self.log_file}")
        print(f"[*] Alerts saved to: {self.alert_file}")
        print(f"[*] Press Ctrl+C to stop\n")
        
        # Check if log file exists
        if not os.path.exists(self.log_file):
            open(self.log_file, 'w').close()
        
        # Start from end of file
        with open(self.log_file, 'r', encoding='utf-8') as f:
            f.seek(0, 2)  # Go to end
            
            try:
                while True:
                    line = f.readline()
                    if line.strip():
                        print(f"[LOG] {line.strip()}")
                        self.analyze_event(line.strip())
                    else:
                        time.sleep(0.1)
            except KeyboardInterrupt:
                print(f"\n\n[+] Monitoring stopped")
                print(f"[+] Total alerts generated: {self.alerts_count}")
                print(f"[+] Check {self.alert_file} for details")

if __name__ == "__main__":
    monitor = SOCMonitor()
    monitor.start_monitoring()