import os
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from rich import box
from rich.spinner import Spinner
from rich.live import Live
from utils import clear_screen, type_writer  # your utils functions
from stress_methods import run_test

console = Console()

def interactive_main():
    clear_screen()
    # Use your utils.py's ASCII art printing and typing effect
    type_writer("Welcome to PulseStrike\n", delay=0.03)
    # Print the banner
    console.print(Panel("PulseStrike", title="PulseStrike", border_style="bold green"), justify="center")
    type_writer("A tool for stress testing your web applications.\n", delay=0.03)
    type_writer("Please use responsibly.\n", delay=0.03)

    url = Prompt.ask("[cyan]Enter target URL[/cyan]", default="http://example.com")
    
    methods = ["GET", "POST", "HEAD"]
    method_list = "\n".join(f"[bold cyan]{i}. {m}[/bold cyan]" for i, m in enumerate(methods, 1))
    console.print(Panel(method_list, title="[bold green]Select HTTP Method[/bold green]", box=box.ROUNDED))

    method_choice = IntPrompt.ask("Enter method number", choices=[str(i) for i in range(1, len(methods)+1)])
    method = methods[method_choice - 1]

    delay = IntPrompt.ask("Enter delay between requests (seconds)", default=1)

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0)"
    ]

    console.print(Panel(f"[yellow]Starting test:[/yellow] [bold]{method}[/bold] requests to [bold]{url}[/bold] every {delay} second(s).", box=box.ROUNDED))

    with Live(Spinner("dots", text="Sending test request..."), refresh_per_second=10):
        run_test(url, method, delay, user_agents)

    console.print(f"[green]Test sent![/green] Check your server and logs to verify the hit.")

def main():
    try:
        interactive_main()
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}", style="bold red")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
