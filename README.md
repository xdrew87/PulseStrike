# PulseStrike - Lightweight C2 Stress Testing Tool

![PulseStrike](https://img.shields.io/badge/PulseStrike-C2%20Stress%20Tool-green)

PulseStrike is a lightweight and interactive Command & Control (C2)-style tool used for stress testing websites and services. It includes a hacker-themed UI and multiple HTTP-based test methods to help you determine how your site performs under heavy traffic or simulated attack conditions.

> ⚠️ This tool is for educational and authorized testing purposes only. Do not use it on servers or systems you do not own or have explicit permission to test.

---

## 🚀 Features

- Terminal interface with animated ASCII banner  
- Real-time logs, bandwidth monitoring, and request counters  
- Interactive prompts — no need to type commands manually  
- Multiple built-in stress test methods  
- Easily extendable — add your own methods in `stress_methods.py`  
- Cross-platform compatible (Windows, Linux, macOS)

---

## 💻 Installation

Make sure you have Python 3.8+ installed.

Clone the repository and install the required dependencies:

```
git clone https://github.com/xdrew87/pulsestrike.git
cd pulsestrike
pip install -r requirements.txt
```

---

## 🛠️ Usage

Run the tool:

```
python pulse.py



Then follow the prompts:

- Enter the target URL (e.g. https://example.com)  
- Choose the attack method  
- Specify delay between requests  
- Watch live logs and bandwidth usage  
- Press CTRL+C to stop the test

---

## 📦 Available Stress Test Methods

- GET — Basic HTTP GET flood  
- POST — HTTP POST flood with randomized data  
- HEADERS — Flood using randomized HTTP headers  

You can add your own by modifying `stress_methods.py`.

```
```
```

## 📸 Screenshots
![Screenshot_From_2025-05-16_04-19-12](https://github.com/user-attachments/assets/c3e6b76c-1a02-4017-a52b-3210ef0c1cf1)
```
```
```
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Open issues for bugs or feature requests  
- Submit pull requests for new methods or improvements  
- Suggest UI/UX enhancements  

Please follow standard GitHub etiquette and code of conduct.

---

## ⚠️ Disclaimer

This tool is intended strictly for authorized testing and educational use. Misuse on unauthorized targets is illegal. The author assumes no responsibility for damage or legal consequences caused by improper usage.

---

## 📬 Contact

- Discord: suicixde  
- GitHub: [xdrew87](https://github.com/xdrew87)

---

## 🪪 License

GNU License © 2025 Suicixde
