#!/usr/bin/python3
"""This module provide test cases for the file storage file which handles the serialization and deserialization"""
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """This method set up the test environment."""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.name = "Test_Model"
        self.model.my_number = 42

    def tearDown(self):
        """This method clean up the test environment."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_new_method(self):
        """This method test the new method of FileStorage."""
        self.storage.new(self.model)
        self.assertIn(type(self.model).__name__ + '.' + self.model.id, self.storage.all())

    def test_save_method(self):
        """This method test the save method of FileStorage."""
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

if __name__ == '__main__':
    unittest.main()

