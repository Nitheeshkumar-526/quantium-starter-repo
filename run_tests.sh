#!/bin/bash

# Exit immediately if any command fails
set -e

# Activate virtual environment
source venv/bin/activate

# Run tests
python -m pytest

# If we reach here, tests passed
exit 0
