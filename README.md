# PulseStrike

PulseStrike is a lightweight and ethical HTTP stress-testing tool used to evaluate the performance and resilience of your own web servers.

🛡️ For authorized use only!

## Usage
python3 pulse.py -u https://yoursite.com -m GET -t 10 -d 1.0

Options:
- -u / --url      Target URL
- -m / --method   HTTP method: GET, POST, HEAD
- -t / --threads  Number of threads
- -d / --delay    Delay between requests (seconds)

## License
MIT
