#!/usr/bin/python3
"""The is the unittest file for base_model"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):
    """This class define test cases for the base_model in different scenerios"""

    def setUp(self):
        """
        This method set up a new instance of the BaseModel class before each test.
        """
        self.model = BaseModel()

    def tearDown(self):
        """
        This method tear down (clean up) resources after each test.
        """
        del self.model

    def test_instance_attributes(self):
        """
        This method test if the instance has the required attributes.
        """
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_is_string(self):
        """
        This method test if the 'id' attribute is of type string.
        """
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        """
        This method test if the 'created_at' attribute is of type datetime.
        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        This method test if the 'updated_at' attribute is of type datetime.
        """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """
        This method test the __str__ method of the BaseModel class.
        """
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, str(self.model.__dict__))
        self.assertEqual(str(self.model), expected_str)

    def test_save_method(self):
        """
        This method test the save method to ensure 'updated_at' is updated.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """
        This method test the to_dict method to ensure correct dictionary format.
        """
        model_dict = self.model.to_dict()
        self.assertTrue('__class__' in model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)
        self.assertTrue('id' in model_dict)

    def test_to_dict_datetime_format(self):
        """
        This method test if the to_dict method returns datetime strings in the correct format.
        """
        model_dict = self.model.to_dict()
        created_at_str = model_dict['created_at']
        updated_at_str = model_dict['updated_at']
        datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(datetime.strptime(created_at_str, datetime_format), self.model.created_at)
        self.assertEqual(datetime.strptime(updated_at_str, datetime_format), self.model.updated_at)

if __name__ == '__main__':
    unittest.main()

