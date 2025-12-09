# Advent of Code 2025

Solutions for Advent of Code 2025 challenges in Python.

## Setup

### Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

### Install the project:
```bash
pip install -e .
```
(Optional) - install dev tools:
```bash
pip install -e ".[dev]"

## Project Structure

```
AoC2025/
├── solutions/          # Solution files for each day
├── inputs/             # Input files for each day
├── utils/              # Shared utilities
├── venv/               # Virtual environment
├── pyproject.toml      # Project configuration
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

## Running Solutions

Each solution should be run as a module:
```bash
python solutions/day01.py
```

## Notes

- Input files should be stored in the `inputs/` folder
- Shared functions should go in the `utils/` folder
- Each day's solution can be a standalone Python file
