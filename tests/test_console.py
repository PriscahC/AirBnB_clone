#!/usr/bin/python3
"""Defines unittests for console.py.

"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


if __name__ == "__main__":
    unittest.main()
