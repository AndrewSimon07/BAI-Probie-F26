"""
Main Module

This is the entry point of the agent application. It orchestrates three AI agents
to process user input through a multi-step pipeline.

Key Concepts:
- Agent Orchestration: Coordinating multiple agents to work together
- Async/Await: Using asynchronous programming for API calls
- Error Handling: Gracefully managing errors at each step
- Sequential Processing: Each agent builds on the previous agent's work

The pipeline:
1. Get input from user
2. Run Agent One to process initial input
3. Run Agent Two to analyze Agent One's output
4. Run Agent Three to synthesize everything
5. Display final report
6. Ask if user wants to continue
"""

import asyncio
from src.agent.models import FinalReport
from src.agent.sub_agents.agent_one import run_agent_one
from src.agent.sub_agents.agent_two import run_agent_two
from src.agent.sub_agents.agent_three import run_agent_three
from src.agent import ui
from src.utils.debug import debug_log


def should_quit(user_input: str) -> bool:
    """
    Check if the user wants to quit the application.
    
    Args:
        user_input: The user's input
        
    Returns:
        True if user wants to quit, False otherwise
    """
    quit_commands = {"quit", "exit", "bye", "q"}
    return user_input.lower() in quit_commands


async def process_input(user_input: str) -> FinalReport:
    """
    Orchestrate all three agents to process the user's input.

    This function coordinates Agent One, Two, and Three to produce
    a complete final report.

    Args:
        user_input: The user's input to process

    Returns:
        FinalReport with outputs from all three agents

    Process:
        1. Agent One processes the initial input
        2. Agent Two analyzes Agent One's output
        3. Agent Three synthesizes everything into a final result
        4. All outputs are combined into a FinalReport
    """
    # Step 1: Run Agent One
    ui.display_loading("Step 1 of 3: Processing input with Agent One...")
    agent_one_output = await run_agent_one(user_input)

    # Step 2: Run Agent Two
    ui.display_loading("Step 2 of 3: Analyzing with Agent Two...")
    agent_two_output = await run_agent_two(agent_one_output)

    # Step 3: Run Agent Three
    ui.display_loading("Step 3 of 3: Synthesizing final output with Agent Three...")
    agent_three_output = await run_agent_three(agent_one_output, agent_two_output)

    # Create final report
    report = FinalReport(
        user_input=user_input,
        agent_one_output=agent_one_output,
        agent_two_output=agent_two_output,
        agent_three_output=agent_three_output,
    )
    return report


async def run_main_loop() -> None:
    """
    Main processing loop - the heart of the application!

    This function:
    1. Displays the welcome message
    2. Gets input from user
    3. Orchestrates the three agents
    4. Displays the final report
    5. Asks if user wants to continue
    6. Handles errors gracefully
    """
    ui.display_welcome()

    while True:
        try:
            # Get input from user
            user_input = ui.get_user_input()

            # Check if user wants to quit
            if should_quit(user_input):
                debug_log("User requested to quit")
                ui.display_goodbye()
                break

            # Validate input
            if not user_input.strip():
                ui.display_error("Please enter some input!")
                continue

            # Process the input through all three agents
            try:
                report = await process_input(user_input)
                # Display the complete report
                ui.display_report(report)

            except ValueError as e:
                ui.display_error(str(e))
                continue
            except Exception as e:
                ui.display_error(f"An unexpected error occurred: {str(e)}")
                debug_log(f"Error details: {e}")
                continue

            # Ask if user wants to continue
            if not ui.ask_continue():
                ui.display_goodbye()
                break
            else:
                debug_log("User chose to continue - starting new processing loop")
                
        except KeyboardInterrupt:
            # User pressed Ctrl+C
            print()  # New line after ^C
            ui.display_goodbye()
            break
        except Exception as e:
            # Unexpected error in the main loop
            ui.display_error(f"Fatal error: {str(e)}")
            break


def main() -> None:
    """
    Entry point for the agent application.

    This function is called when you run: python -m src.agent.main
    It sets up the async environment and runs the main loop.
    """
    try:
        # Run the main loop
        asyncio.run(run_main_loop())
    except KeyboardInterrupt:
        print("\n")
        ui.display_goodbye()
    except Exception as e:
        ui.display_error(f"Failed to start: {str(e)}")


if __name__ == "__main__":
    main()

