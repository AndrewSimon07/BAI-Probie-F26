"""
Filesystem Utility Module

This module provides utility functions for working with the filesystem.
"""

import pathlib


def get_project_root() -> pathlib.Path:
    """
    Get the root directory of the project.
    
    This function navigates up from the current file to find the project root.
    It's useful for locating configuration files like .env
    
    Returns:
        Path object pointing to the project root directory
    """
    return pathlib.Path(__file__).parent.parent.parent

