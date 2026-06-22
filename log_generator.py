#!/usr/bin/env python3
"""
SOC Log Generator - Simple Version
Generates simulated security events for testing
"""

import time
import random
from datetime import datetime
import os
import sys

class SecurityLogGenerator:
    def __init__(self, log_file="security_events.log"):
        self.log_file = log_file
        self.ip_pool = [
            "192.168.1.100", "10.0.0.45", "172.16.0.23", 
            "203.0.113.50", "198.51.100.22", "192.168.2.155",
            "45.33.32.156", "104.236.198.203", "159.89.121.45"
        ]
        self.users = ["admin", "john.doe", "sarah.smith", "guest", "root", "svc_backup"]
        
        self.events = [
            ("Successful login for user {user} from {ip}", 30),
            ("Connection closed by {ip} port 443", 20),
            ("User {user} changed password successfully", 15),
            ("File backup completed for {user}", 10),
            ("User {user} logged out successfully", 15),
            ("Failed password for {user} from {ip} port 22 ssh2", 10),
            ("User {user} accessed sensitive file /etc/shadow", 5),
            ("403 Forbidden - {user} attempted to access /admin from {ip}", 5),
            ("Multiple connection attempts from {ip}", 3),
            ("Unusual login time for user {user} from {ip}", 3),
            ("Possible malware detected in file upload from {user}", 1),
            ("SQL injection attempt detected from {ip}", 3),
            ("Port scan detected from {ip}", 3),
            ("New admin account created by {user} from {ip}", 1),
            ("Firewall blocked incoming connection from {ip}", 5)
        ]
        
        self.weighted_events = []
        for event, weight in self.events:
            self.weighted_events.extend([event] * weight)
    
    def generate_log(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        event_template = random.choice(self.weighted_events)
        event = event_template.format(
            user=random.choice(self.users),
            ip=random.choice(self.ip_pool)
        )
        log_entry = f"{timestamp} - {event}\n"
        
        with open(self.log_file, "a", encoding='utf-8') as f:
            f.write(log_entry)
        
        return log_entry.strip()

def main():
    print("="*50)
    print("  SOC Log Generator - Generating Events")
    print("="*50)
    print("[*] Press Ctrl+C to stop\n")
    
    generator = SecurityLogGenerator()
    count = 0
    
    try:
        while True:
            log = generator.generate_log()
            print(f"[{count+1}] {log}")
            count += 1
            time.sleep(1)  # Generate 1 log per second
            
    except KeyboardInterrupt:
        print(f"\n\n[+] Generated {count} log entries")
        print(f"[+] Log file: {os.path.abspath(generator.log_file)}")

if __name__ == "__main__":
    main()