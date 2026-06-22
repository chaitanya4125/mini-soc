# 🛡️ Mini SOC - Real-Time Security Operations Center Simulator

A lightweight, real-time Security Operations Center (SOC) simulator built using Python and standard web technologies. This project demonstrates core SOC concepts including log monitoring, threat detection, alert generation, and dashboard visualization.

---

## 🚀 Features

* Real-time security event generation
* Rule-based threat detection engine
* Interactive web dashboard
* Live alert monitoring
* REST API endpoints
* Zero external dependencies
* Configurable detection rules

---

## 🔧 Manual Method (All Platforms)

### Step 1: Start the HTTP Server

```bash
python server.py
```

### Step 2: Generate Security Events (Open a New Terminal)

```bash
python log_generator.py
```

### Step 3: Start Threat Monitor (Open Another New Terminal)

```bash
python soc_monitor.py
```

### Step 4: Open Dashboard

Open your browser and navigate to:

```text
http://localhost:8000/dashboard.html
```

---

## 📁 Project Structure

```text
mini-soc/
│
├── server.py             # HTTP server with REST API endpoints
├── log_generator.py      # Realistic security event generator
├── soc_monitor.py        # Real-time threat detection engine
├── alert_rules.json      # Configurable detection rules
├── dashboard.html        # Interactive web dashboard
├── run_soc.bat           # Windows one-click launcher
├── .gitignore            # Git ignore configuration
├── LICENSE               # MIT License
└── README.md             # Project documentation
```

---

## 🎯 Detection Rules

The system includes six pre-configured detection rules:

| Rule ID  | Name                 | Pattern               | Threshold | Window | Severity    |
| -------- | -------------------- | --------------------- | --------- | ------ | ----------- |
| RULE-001 | Brute Force Attack   | Failed password       | 5 events  | 60s    | 🔴 CRITICAL |
| RULE-002 | SQL Injection        | sql injection         | 1 event   | 10s    | 🔴 CRITICAL |
| RULE-003 | Malware Detection    | malware detected      | 1 event   | 10s    | 🔴 CRITICAL |
| RULE-004 | Unauthorized Access  | 403 Forbidden         | 3 events  | 30s    | 🟡 HIGH     |
| RULE-005 | Privilege Escalation | admin account created | 1 event   | 30s    | 🔴 CRITICAL |
| RULE-006 | Port Scanning        | port scan             | 3 events  | 20s    | 🟠 MEDIUM   |

---

## 📊 Dashboard Features

### 📈 Live Statistics Panel

* Total events processed
* Alerts by severity (Critical, High, Medium, Low)
* Real-time counter animations
* Connection status indicator

### 🚨 Alert Feed

* Color-coded alerts based on severity
* Timestamp and rule information
* Matched event count
* Animated slide-in effects

### 📜 Event Log Viewer

Streaming security events in real time.

Color Coding:

* 🔴 Red → Malicious events (Malware, SQL Injection)
* 🟡 Orange → Suspicious events (Failed Logins, Forbidden Access)
* ⚪ Gray → Normal events

---

## 🛠️ Technologies Used

| Component    | Technology                        |
| ------------ | --------------------------------- |
| Backend      | Python 3 (`http.server`)          |
| Frontend     | HTML5, CSS3, JavaScript (Vanilla) |
| Data Format  | JSON                              |
| API          | REST Endpoints                    |
| Styling      | CSS Grid, Flexbox, Animations     |
| Dependencies | None (Standard Library Only)      |

### Python Standard Library Modules Used

* `http.server` → HTTP server implementation
* `json` → Data parsing and serialization
* `re` → Pattern matching using regular expressions
* `datetime` → Timestamp handling
* `collections` → defaultdict and data structures
* `threading` → Concurrent processing (optional)
* `os` and `sys` → System operations

---

## 📈 Sample Output

### Console Monitor Output

```text
==================================================
  SOC MONITOR - Real-time Threat Detection
==================================================
[*] Monitoring: security_events.log

🔴 ALERT #1: CRITICAL - Brute Force Attack
   Time: 2024-01-15 10:30:25
   Events: 5 failed login attempts detected

🔴 ALERT #2: CRITICAL - SQL Injection Attempt
   Time: 2024-01-15 10:31:10
   Events: SQL injection pattern detected

==================================================
     MONITORING SUMMARY
==================================================
  Duration: 0:05:23
  Events Processed: 156
  Alerts Generated: 12

  Alerts by Severity:
    CRITICAL: 8
    HIGH: 3
    MEDIUM: 1
    LOW: 0
```

---

## 🖥️ Dashboard Overview

The dashboard displays:

* Statistics cards showing total events and alert counts
* Live alert feed with color-coded entries
* Streaming security event logs
* Start, Stop, Refresh, and Clear controls
* Green pulsing indicator showing connection status

---

## 🔧 Customization Guide

### ➕ Adding New Detection Rules

Edit `alert_rules.json`:

```json
{
  "id": "RULE-007",
  "name": "Data Exfiltration",
  "pattern": "large file transfer|data export",
  "threshold": 2,
  "time_window": 60,
  "severity": "HIGH",
  "description": "Possible data exfiltration detected"
}
```

### 📝 Modifying Event Generation

Edit the event list in `log_generator.py`:

```python
self.events = [
    ("Your custom event {user} from {ip}", 10)
]
```

### ⏱️ Changing Dashboard Refresh Rate

Inside `dashboard.html`:

```javascript
monitoringInterval = setInterval(refreshData, 3000);
// 3000ms = 3 seconds
```

### 🎨 Customizing Alert Colors

```css
.CRITICAL {
    border-color: #ff4444;
}

.HIGH {
    border-color: #ffaa00;
}
```

---

## 🎓 Learning Resources

### Key Concepts Demonstrated

* Log Analysis
* Pattern Matching using Regex
* SIEM Concepts
* Alert Triage
* Dashboard Design
* REST API Development

---

## 🤝 Contributing

Contributions are welcome.

## 🐛 Troubleshooting

### Dashboard Shows All Zeros

* Ensure `server.py` is running.
* Verify the dashboard URL.
* Confirm log files are being generated.

### Port 8000 Already in Use

```bash
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

Or change the port:

```python
PORT = 3000
```

## 🚀 Deployment Options

### Option 1: Local Development

```bash
python server.py
```

Access:

```text
http://localhost:8000
```

### Option 2: Network Access

Modify:

```python
HOST = "0.0.0.0"
```

Access from another machine:

```text
http://YOUR_IP:8000
```

### Option 3: GitHub Pages (Dashboard Only)

Enable GitHub Pages from repository settings for static demonstrations.

---

## 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for complete details.

---

## ⭐ Show Your Support

If this project helped you:

* ⭐ Star the repository
* 🍴 Fork and customize it
* 📢 Share with others
* 🐛 Report issues

---

## 🙏 Acknowledgments

* Inspired by real-world SOC operations
* Built for cybersecurity education
* Dedicated to the InfoSec community

<div align="center">

### Made with ❤️ for Cybersecurity Learners

*"Security is not a product, but a process."* — Bruce Schneier

</div>

---

