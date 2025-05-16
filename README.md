# PulseStrike - Lightweight C2 Stress Testing Tool

![PulseStrike Banner](https://img.shields.io/badge/PulseStrike-C2%20Stress%20Tool-green)

## Overview

PulseStrike is a simple yet powerful Command & Control (C2) tool designed for stress testing your websites and servers. Easily simulate various attack methods to test your defenses and evaluate your infrastructure's resilience.

This tool enables you to:

- Launch multiple HTTP stress tests against a target URL
- Monitor requests and bandwidth usage in real-time via a sleek terminal UI
- Quickly configure targets, methods, and delays from the interactive console

> **Disclaimer:** Use PulseStrike only on servers and websites you own or have explicit permission to test. Unauthorized use is illegal and unethical.

---

## Features

- Multiple stress test methods (GET, POST, headers flooding, etc.)
- Real-time request log with bandwidth statistics
- Animated ASCII art banner and hacker-style terminal UI
- Cross-platform compatibility (Windows, Linux, macOS)
- Easy extensibility for custom attack methods

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

```bash
git clone https://github.com/yourusername/pulsestrike.git
cd pulsestrike
pip install -r requirements.txt

#Usage
Run the tool:
python pulse.py
Enter the target URL when prompted.

Choose the attack method from the displayed list.

Specify the delay between requests (seconds).

Monitor the real-time logs and bandwidth usage.

Press CTRL+C to stop the test.

#Available Stress Test Methods
GET — Basic HTTP GET flood

POST — HTTP POST flood with randomized data

HEADERS — Flood using randomized HTTP headers

Extendable via stress_methods.py.

Contributing
Contributions are welcome! Feel free to:

Open issues for bugs or feature requests

Submit pull requests for new methods or improvements

Suggest UI/UX enhancements

Please adhere to the code of conduct.

Disclaimer
This tool is intended strictly for authorized testing and educational purposes. Misuse on unauthorized targets is illegal. The author holds no responsibility for damage or legal issues caused by improper use.

Contact

Discord: suicixde

GitHub: xdrew87

#Screenshots

License
GNU License © 2025 Suicixde
