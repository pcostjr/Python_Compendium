"""
Filename: task.py
Description: File containing the class that represents the tasks on the map.
Author: Tony Le
Created: 10/17/23
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Task:
    name: str
    description: str
