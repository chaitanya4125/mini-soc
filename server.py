#!/usr/bin/env python3
"""
Simple HTTP Server for SOC Dashboard
Solves CORS issues and serves files properly
"""

import http.server
import socketserver
import json
import os
from urllib.parse import urlparse
import sys

PORT = 8000

class SOCHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler for SOC dashboard"""
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        
        # API endpoint for alerts
        if parsed_path.path == '/api/alerts':
            self.send_alerts()
        # API endpoint for events
        elif parsed_path.path == '/api/events':
            self.send_events()
        # API endpoint for stats
        elif parsed_path.path == '/api/stats':
            self.send_stats()
        # Serve static files
        else:
            super().do_GET()
    
    def send_alerts(self):
        """Send alerts as JSON"""
        try:
            alerts = []
            if os.path.exists('alerts.log'):
                with open('alerts.log', 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            try:
                                alert = json.loads(line)
                                alerts.append(alert)
                            except:
                                pass
            
            self.send_json_response(alerts)
        except Exception as e:
            self.send_json_response({'error': str(e)}, 500)
    
    def send_events(self):
        """Send recent events as JSON"""
        try:
            events = []
            if os.path.exists('security_events.log'):
                with open('security_events.log', 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    # Get last 100 events
                    recent_lines = lines[-100:] if len(lines) > 100 else lines
                    events = [line.strip() for line in recent_lines if line.strip()]
            
            self.send_json_response(events)
        except Exception as e:
            self.send_json_response({'error': str(e)}, 500)
    
    def send_stats(self):
        """Send statistics as JSON"""
        try:
            stats = {
                'total_alerts': 0,
                'critical': 0,
                'high': 0,
                'medium': 0,
                'low': 0,
                'total_events': 0
            }
            
            # Count alerts
            if os.path.exists('alerts.log'):
                with open('alerts.log', 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            try:
                                alert = json.loads(line)
                                stats['total_alerts'] += 1
                                severity = alert.get('severity', '').lower()
                                if severity == 'critical':
                                    stats['critical'] += 1
                                elif severity == 'high':
                                    stats['high'] += 1
                                elif severity == 'medium':
                                    stats['medium'] += 1
                                elif severity == 'low':
                                    stats['low'] += 1
                            except:
                                pass
            
            # Count events
            if os.path.exists('security_events.log'):
                with open('security_events.log', 'r', encoding='utf-8') as f:
                    stats['total_events'] = len(f.readlines())
            
            self.send_json_response(stats)
        except Exception as e:
            self.send_json_response({'error': str(e)}, 500)
    
    def send_json_response(self, data, status=200):
        """Send JSON response with proper headers"""
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
    
    def log_message(self, format, *args):
        """Custom log format"""
        sys.stdout.write(f"[SOC Server] {args[0]}\n")

def main():
    """Start the HTTP server"""
    # Change to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("="*60)
    print("  🛡️  SOC DASHBOARD SERVER")
    print("="*60)
    print(f"\n  Server running at: http://localhost:{PORT}")
    print(f"  Dashboard: http://localhost:{PORT}/dashboard.html")
    print(f"\n  Press Ctrl+C to stop the server\n")
    print("="*60)
    
    try:
        with socketserver.TCPServer(("", PORT), SOCHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n[+] Server stopped")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"\n[!] Port {PORT} is already in use!")
            print("[*] Try closing other programs or change PORT in server.py")
        else:
            print(f"\n[!] Error: {e}")

if __name__ == "__main__":
    main()