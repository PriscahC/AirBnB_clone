#!/usr/bin/python3
<<<<<<< HEAD
"""This module creates a User class, Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):

    """Class for managing state objects
    Represent a state.
    Attributes:
        name (str): The name of the state.
    """

=======
"""This module creates the state class that inherits from BaseModel class"""

from models.base_model import BaseModel

class State(BaseModel):
    """State class"""
    
>>>>>>> 68e17e9553bd6328a558c2906fa00edd5f05534a
    name = ""
