#!/usr/bin/python3
<<<<<<< HEAD
"""This module creates a User class, Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects
    Represent a User.
    Attributes:
        email (str): the email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): the last name of the user.
    """

=======
"""This module creates a class User that inherits from BaseModel"""
from models.base_model import BaseModel

class User(BaseModel):
    """User class"""
    
>>>>>>> 68e17e9553bd6328a558c2906fa00edd5f05534a
    email = ""
    password = ""
    first_name = ""
    last_name = ""
