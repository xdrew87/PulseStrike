from rich.console import Console
from rich.panel import Panel
import time
import os
import sys
from datetime import datetime
from threading import Thread
from queue import Queue, Empty
from rich.live import Live
from rich.align import Align
from rich.layout import Layout
from rich.box import ROUNDED


console = Console()

ASCII_BANNER = """
██████╗ ██╗   ██╗██╗     ███████╗███████╗████████╗███████╗██████╗ 
██╔══██╗██║   ██║██║     ██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╔╝██║   ██║██║     █████╗  ███████╗   ██║   █████╗  ██████╔╝
██╔═══╝ ██║   ██║██║     ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔═══╝ 
██║     ╚██████╔╝███████╗███████╗███████║   ██║   ███████╗██║     
╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝     
"""

def print_banner():
    banner = """[bold green]
██████╗ ██╗   ██╗██╗     ███████╗███████╗████████╗███████╗██████╗ 
██╔══██╗██║   ██║██║     ██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╔╝██║   ██║██║     █████╗  ███████╗   ██║   █████╗  ██████╔╝
██╔═══╝ ██║   ██║██║     ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔═══╝ 
██║     ╚██████╔╝███████╗███████╗███████║   ██║   ███████╗██║     
╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝     
[/bold green]"""
    console.print(banner)
    time.sleep(0.5)

def disclaimer():
    message = "[bold red][!] For educational and authorized testing only. Unauthorized use is prohibited.[/bold red]"
    console.print(Panel(message, title="⚠️ WARNING", border_style="red"))
    time.sleep(0.5)

def load_user_agents():
    try:
        with open("user_agents.txt") as f:
            return [ua.strip() for ua in f.readlines() if ua.strip()]
    except:
        return ["Mozilla/5.0"]

def log_request(url, method):
    from datetime import datetime
    with open("logs.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sent {method} request to {url}\n")

def clear_screen():
    """Clear the terminal screen in a cross-platform way."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer(text, delay=0.05):
    """Print text like a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline at end

def glitch_text(text, iterations=3, delay=0.05):
    chars = list(text)
    for _ in range(iterations):
        for i in range(len(chars)):
            if chars[i] != ' ' and os.urandom(1)[0] % 5 == 0:
                chars[i] = chr(33 + os.urandom(1)[0] % 94)
        console.print("".join(chars), style="bold green")
        time.sleep(delay)
        clear_screen()
    console.print(text, style="bold green")

def build_layout(log_messages, target_url, method, delay):
    layout = Layout()

    banner_panel = Panel(Align.center(ASCII_BANNER), style="green on black", box=ROUNDED)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    info_text = f"[bold]Target URL:[/bold] {target_url}\n[bold]Method:[/bold] {method}\n[bold]Delay:[/bold] {delay}s\n[bold]Time:[/bold] {now}"
    info_panel = Panel(info_text, title="Session Info", style="green on black", box=ROUNDED)

    log_panel = Panel(
        "\n".join(log_messages[-15:]) if log_messages else "Waiting for commands...",
        title="Request Log",
        style="green on black",
        box=ROUNDED,
        height=15,
        subtitle="[dim]Press Ctrl+C to exit[/dim]"
    )

    layout.split(
        Layout(banner_panel, size=7),
        Layout(name="main", ratio=1)
    )
    layout["main"].split_row(
        Layout(info_panel, size=40),
        Layout(log_panel)
    )

    return layout

def live_log_thread(run_test_func, url, method, delay, user_agents, q: Queue):
    while True:
        try:
            run_test_func(url, method, delay, user_agents)
            q.put(f"[green]Sent {method} request to {url} at {datetime.now().strftime('%H:%M:%S')}[/green]")
            time.sleep(delay)
        except Exception as e:
            q.put(f"[red]Error: {e}[/red]")
            break
