#!/bin/bash

KATA_DIR=$(basename $(pwd))

echo "Running flake8 checks for $KATA_DIR..."
flake8 .

echo "Running tests and coverage report for $KATA_DIR..."
pytest --cov=. --cov-report=term-missing 