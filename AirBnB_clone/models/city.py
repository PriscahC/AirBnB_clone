#!/usr/bin/python3
"""This module creates the city class that inherits from BaseModel class"""

from models.base_model import BaseModel

class City(BaseModel):
    """City class"""
    
    state_id = ""
    name = ""