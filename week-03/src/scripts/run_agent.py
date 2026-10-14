#!/usr/bin/env python3
"""Interactive RAG agent chat interface with Rich formatting."""

import asyncio

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.rule import Rule

from src.agent.rag_agent import RAGAgentDependencies, rag_agent
from src.services.embedding.service import EmbeddingService
from src.services.vector_database.service import VectorDatabaseService

console = Console()


async def run_chat():
    """Main chat loop with Rich-formatted interface."""
    console.print(
        Panel.fit(
            "[bold cyan]RAG Agent - Interactive Chat[/bold cyan]\n"
            "[dim]Ask questions about your ingested data[/dim]",
            border_style="cyan",
        )
    )

    with console.status(
        "[bold green]Initializing agent and services...", spinner="dots"
    ):
        embedding_service = EmbeddingService()
        vector_db = VectorDatabaseService(embedding_service=embedding_service)
        dependencies = RAGAgentDependencies(
            vector_db=vector_db, embedder=embedding_service
        )

    console.print("[green]✓[/green] Agent ready!\n")
    console.print("[dim]Commands: Ask any question • 'quit' to exit[/dim]\n")

    while True:
        try:
            user_input = Prompt.ask("[bold cyan]You[/bold cyan]").strip()

            if not user_input:
                continue

            if user_input.lower() in ["quit", "exit", "q"]:
                console.print(
                    Panel(
                        "[bold yellow]Goodbye! 👋[/bold yellow]", border_style="yellow"
                    )
                )
                break

            # Run the agent
            with console.status("[bold blue]Thinking...", spinner="dots"):
                result = await rag_agent.run(user_input, deps=dependencies)

            # Display the response
            console.print()
            console.print(
                Rule("[bold green]Agent Response[/bold green]", style="green")
            )

            # Display the answer
            answer_panel = Panel(
                result.output.answer,
                title="[bold]Answer[/bold]",
                border_style="green",
                box=box.ROUNDED,
                padding=(1, 2),
            )
            console.print(answer_panel)

            # Display sources if available
            if result.output.sources:
                console.print("\n[bold magenta]Sources:[/bold magenta]")
                for i, source in enumerate(result.output.sources, 1):
                    console.print(f"  [dim]{i}.[/dim] [cyan]{source}[/cyan]")
            else:
                console.print("\n[dim]No sources were used for this answer.[/dim]")

            console.print()

        except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted. Goodbye! 👋[/yellow]")
            break
        except Exception as e:
            console.print(f"\n[bold red]Error:[/bold red] {e}\n")


if __name__ == "__main__":
    asyncio.run(run_chat())
