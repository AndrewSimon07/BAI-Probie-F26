"""
User Interface Module

This module provides simple terminal UI functions using the Rich library.
All functions here display information in a clean, easy-to-read format.

Rich is a Python library for rich text and beautiful formatting in the terminal.
It provides colors, tables, panels, and much more!

Customize these functions for your specific use case!
"""

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich import box
from src.agent.models import FinalReport


# Create a global console object for printing
console = Console()


def display_welcome() -> None:
    """
    Display a welcome banner when the application starts.
    """
    welcome_text = """
    # 🤖 Multi-Agent Pipeline Template
    
    Welcome! This is a template for building multi-agent AI applications with **Pydantic AI**.
    
    **How it works:**
    - 🔹 **Agent One**: Processes your initial input
    - 🔸 **Agent Two**: Analyzes Agent One's output  
    - 🔹 **Agent Three**: Synthesizes everything into a final result
    
    **Commands:**
    - Enter any text to process through the agent pipeline
    - Type `quit`, `exit`, or `bye` to end the session
    
    *Customize this template for your own use case!*
    """
    
    panel = Panel(
        Markdown(welcome_text),
        title="Welcome",
        border_style="bright_blue",
        box=box.ROUNDED,
        padding=(1, 2),
    )
    
    console.print(panel)
    console.print()


def display_loading(message: str = "Processing...") -> None:
    """
    Display a loading message while processing.
    
    Args:
        message: Custom loading message
    """
    console.print(f"[dim]⏳ {message}[/dim]")


def display_error(error_message: str) -> None:
    """
    Display an error message in red.
    
    Args:
        error_message: Description of the error
    """
    console.print(f"[bold red]❌ Error:[/bold red] {error_message}")
    console.print()


def get_user_input() -> str:
    """
    Prompt the user for input.
    
    Returns:
        The user's input (stripped of whitespace)
    """
    user_input = Prompt.ask("[bold cyan]Enter your input[/bold cyan]")
    return user_input.strip()


def display_report(report: FinalReport) -> None:
    """
    Display the complete final report from all three agents.
    
    This shows the outputs from each agent in a structured format.
    Customize this for your specific use case!
    
    Args:
        report: Complete FinalReport object
    """
    console.print()
    console.print("[bold bright_blue]" + "=" * 70 + "[/bold bright_blue]")
    console.print()
    
    # Display original input
    console.print(Panel(
        f"[cyan]{report.user_input}[/cyan]",
        title="📥 Original Input",
        border_style="cyan",
        box=box.ROUNDED,
    ))
    console.print()
    
    # Display Agent One output
    console.print(Panel(
        f"[bold]Data:[/bold] {report.agent_one_output.data}\n"
        f"[bold]Metadata:[/bold] {report.agent_one_output.metadata}",
        title="🔹 Agent One Output",
        border_style="blue",
        box=box.ROUNDED,
    ))
    console.print()
    
    # Display Agent Two output
    console.print(Panel(
        f"[bold]Result:[/bold] {report.agent_two_output.result}\n\n"
        f"[bold]Analysis:[/bold] {report.agent_two_output.analysis}",
        title="🔸 Agent Two Output",
        border_style="yellow",
        box=box.ROUNDED,
    ))
    console.print()
    
    # Display Agent Three output (final)
    console.print(Panel(
        f"[bold]Final Output:[/bold]\n{report.agent_three_output.final_output}\n\n"
        f"[bold]Summary:[/bold]\n{report.agent_three_output.summary}",
        title="✨ Agent Three - Final Result",
        border_style="green",
        box=box.ROUNDED,
    ))
    console.print()
    
    console.print("[bold bright_blue]" + "=" * 70 + "[/bold bright_blue]")
    console.print()


def display_goodbye() -> None:
    """
    Display a farewell message when the user quits.
    """
    goodbye_text = """
    # 👋 Goodbye!
    
    Thanks for using the Multi-Agent Pipeline Template!
    
    Remember to customize this template for your own use case. Happy building! 🚀
    """
    
    panel = Panel(
        Markdown(goodbye_text),
        border_style="bright_blue",
        box=box.ROUNDED,
    )
    
    console.print(panel)


def ask_continue() -> bool:
    """
    Ask if the user wants to process another input.
    
    Returns:
        True if the user wants to continue, False otherwise
    """
    response = Prompt.ask(
        "\n[bold cyan]Process another input?[/bold cyan]",
        choices=["y", "n"],
        default="y"
    )
    return response.lower() == "y"
