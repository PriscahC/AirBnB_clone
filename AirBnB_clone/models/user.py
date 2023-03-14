#!/usr/bin/python3
"""This module creates a class User that inherits from BaseModel"""
from models.base_model import BaseModel

class User(BaseModel):
    """User class"""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""