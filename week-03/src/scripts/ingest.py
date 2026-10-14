#!/usr/bin/env python3
"""Interactive fact ingestion script with Rich formatting."""

import asyncio

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from src.services.embedding.service import EmbeddingService
from src.services.vector_database.service import VectorDatabaseService

console = Console()


async def ingest():
    """Main ingestion loop with Rich-formatted interface."""
    console.print(
        Panel.fit(
            "[bold cyan]Vector Database Fact Ingestion Tool[/bold cyan]",
            border_style="cyan",
        )
    )

    with console.status("[bold green]Initializing services...", spinner="dots"):
        embedding_service = EmbeddingService()
        vector_db = VectorDatabaseService(embedding_service=embedding_service)

    console.print("[green]✓[/green] Ready!\n")
    console.print(
        "[dim]Commands: Type facts to ingest • 'search' to search • 'quit' to exit[/dim]\n"
    )

    while True:
        try:
            user_input = Prompt.ask("[bold cyan]>>>[/bold cyan]").strip()

            if not user_input:
                continue

            if user_input.lower() in ["quit", "exit", "q"]:
                console.print(
                    Panel(
                        "[bold yellow]Goodbye! 👋[/bold yellow]", border_style="yellow"
                    )
                )
                break

            elif user_input.lower() == "search":
                query = Prompt.ask("[bold magenta]Search query[/bold magenta]").strip()
                if query:
                    with console.status("[bold blue]Searching...", spinner="dots"):
                        results = await vector_db.query(query)

                    documents = results["documents"][0]
                    distances = results.get("distances", [[]])[0]

                    if not documents:
                        console.print("[yellow]No results found.[/yellow]\n")
                    else:
                        table = Table(
                            title=f"[bold]Search Results for: {query}[/bold]",
                            box=box.ROUNDED,
                            show_header=True,
                            header_style="bold magenta",
                        )
                        table.add_column("#", style="dim", width=4)
                        table.add_column("Document", style="cyan")
                        table.add_column(
                            "Distance", justify="right", style="green", width=12
                        )

                        for i, (doc, dist) in enumerate(zip(documents, distances), 1):
                            table.add_row(str(i), doc, f"{dist:.4f}")

                        console.print()
                        console.print(table)
                        console.print()

            else:
                # Ingest the fact
                with console.status("[bold green]Ingesting fact...", spinner="dots"):
                    fact_id = await vector_db.add_fact(user_input)

                console.print(
                    f"[green]✓[/green] Ingested successfully "
                    f"[dim](ID: {fact_id[:8]}...)[/dim]\n"
                )

        except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted. Goodbye! 👋[/yellow]")
            break
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}\n")


if __name__ == "__main__":
    asyncio.run(ingest())
