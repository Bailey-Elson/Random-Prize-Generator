#!/bin/bash
source ~/.bashrc
pip3 show coverage
python3 -m coverage run -m pytest testing/test.py
python3 -m coverage report -m