# Advent of Code 2025

Solutions for Advent of Code 2025 challenges in Python.

## How to use this repository

To work on your own solutions and keep them separate from others:

1. **Clone the repository:**
	```bash
	git clone https://github.com/ovanoss-syntech/AoC2025.git
	cd AoC2025
	```
2. **Create a new branch for your solutions:**
	```bash
	git checkout -b your-username-solutions
	```
3. **Add your solution files in the `solutions/` folder.**
4. **To view others' solutions, check out their branch!**

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
```

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
