# settings.py
# Handles settings


# Imports
from typing import Any

import json


# Definitions
def load() -> dict:
    """Load the settings"""
    
    with open("settings.json", 'rt') as file:
        json_data = json.load(file)
    
    return json_data
    

def get(name: str) -> Any:
    return load()[name]