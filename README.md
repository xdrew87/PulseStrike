#PulseStrike - Lightweight C2 Stress Testing Tool

#Overview
PulseStrike is a simple yet powerful Command & Control (C2) tool designed for stress testing your websites and servers. Easily simulate various attack methods to test your defenses and see if your infrastructure can handle real-world traffic scenarios.

This tool allows you to:

Send multiple types of HTTP stress tests to your target URL

Monitor request logs in real-time via a sleek terminal UI

View session info such as target URL, attack method, delay, and bandwidth used

Quickly start tests without complex CLI commands — all from the interactive terminal interface

Note: This tool is intended for ethical testing on servers and websites you own or have explicit permission to test. Do not use it for unauthorized attacks.

#Features
Multiple stress test methods (HTTP floods, randomized user agents, etc.)

Real-time request log and bandwidth output

Animated ASCII art banner and hacker-themed terminal UI

Simple input prompts for target URL, attack method, and delay

Cross-platform clear screen and console output

Easy to extend with new stress test methods

#Installation
Clone the repository:


git clone https://github.com/yourusername/pulsestrike.git
cd pulsestrike
Install required Python dependencies:


pip install -r requirements.txt

Run the tool:

python pulse.py

#Usage
Launch the tool: python pulse.py
Enter the target URL you want to test.
Select the stress test method from the list.
Set the delay between requests (in seconds).
Watch the real-time log and stats as your test runs.
Use CTRL+C to stop the test.


#Stress Test Methods
GET — Basic HTTP GET flood

POST — HTTP POST flood with random data

HEADERS — Flood with randomized headers

Add your custom methods in stress_methods.py

Contributing
Contributions and new stress test methods are welcome! Please open an issue or pull request.

Disclaimer
This tool is for authorized testing and educational purposes only. The author is not responsible for any misuse or damage caused.

Contact
For questions or help, reach out on:

Discord: suicixde

GitHub: xdrew87

Enjoy testing safely! 🚀
