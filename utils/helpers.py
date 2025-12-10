"""Helper functions for parsing and processing input files"""


def read_input(day: int) -> str:
    """Read input file for a specific day.
    
    Args:
        day: Day number (1-25)
        
    Returns:
        Content of the input file
    """
    with open(f"inputs/day{day:02d}.txt", "r") as f:
        return f.read()


def read_lines(day: int) -> list[str]:
    """Read input file and return as list of lines.
    
    Args:
        day: Day number (1-25)
        
    Returns:
        List of lines from the input file
    """
    content = read_input(day)
    return content.strip().split("\n")


def read_numbers(day: int) -> list[int]:
    """Read input file and return as list of integers.
    
    Args:
        day: Day number (1-25)
        
    Returns:
        List of integers from the input file
    """
    return [int(line) for line in read_lines(day)]

def read_test_input(day: int) -> str:
    """Read test input file for a specific day.
    
    Args:
        day: Day number (1-25)
        
    Returns:
        Content of the test input file
    """
    with open(f"inputs/day{day:02d}_test.txt", "r") as f:
        return f.read()


def read_test_lines(day: int) -> list[str]:
    """Read test input file and return as list of lines.
    
    Args:
        day: Day number (1-25)
        
    Returns:
        List of lines from the test input file
    """
    content = read_test_input(day)
    return content.strip().split("\n")


def read_test_numbers(day: int) -> list[int]:
    """Read test input file and return as list of integers.
    
    Args:
        day: Day number (1-25)
        
    Returns:
        List of integers from the test input file
    """
    return [int(line) for line in read_test_lines(day)]
