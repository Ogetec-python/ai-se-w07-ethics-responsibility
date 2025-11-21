"""
utils.py - small helpers for the Week 07 prototype
"""

import json

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
