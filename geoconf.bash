#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the Python script with arguments passed to this script
python main.py "$1" "$2"

# Deactivate the virtual environment
deactivate
