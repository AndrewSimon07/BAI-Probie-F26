"""
Debug Logging Utility

This module provides a simple debug logging function that only prints when debug mode is enabled.
This helps users understand what's happening under the hood in the agentic workflow.

Key Concepts:
- Conditional Logging: Only prints when DEBUG=True in settings
- Consistent Format: All debug messages follow the same format
- Non-intrusive: When debug is disabled, has minimal performance impact

Usage:
    from src.utils.debug import debug_log
    debug_log("Starting data fetch for AAPL")
"""

from src.settings import settings


def debug_log(message: str, *args, **kwargs) -> None:
    """
    Log a debug message if debug mode is enabled.

    This function provides detailed logging of the agentic workflow to help
    users understand what's happening under the hood.

    Args:
        message: The debug message to log
        *args: Additional positional arguments to format into the message
        **kwargs: Additional keyword arguments to format into the message

    Example:
        >>> debug_log("Fetching data for {}", "AAPL")
        [DEBUG] Fetching data for AAPL

        >>> debug_log("Analysis complete", trend="bullish", confidence=0.85)
        [DEBUG] Analysis complete trend=bullish confidence=0.85
    """
    if not settings.DEBUG:
        return

    # Format the message with args if provided
    if args:
        message = message.format(*args)
    elif kwargs:
        # Add kwargs as key=value pairs
        extra_info = " ".join(f"{k}={v}" for k, v in kwargs.items())
        message = f"{message} {extra_info}"

    print(f"[DEBUG] {message}")


def debug_separator(title: str = "") -> None:
    """
    Print a visual separator for organizing debug output.

    Args:
        title: Optional title for the section
    """
    if not settings.DEBUG:
        return

    if title:
        print(f"\n[DEBUG] ===== {title.upper()} =====")
    else:
        print("[DEBUG] --------------------")
