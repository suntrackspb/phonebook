import os


def clear_console() -> None:
    """
    Clears the console.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
