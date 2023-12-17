#!/usr/bin/python3
"""This module is the unittest modeule that test the to_dict """
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_to_dict(self):
        """This method test the to_dict method of BaseModel."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        model_dict = my_model.to_dict()

        expected_keys = ['id', 'created_at', 'updated_at', 'name', 'my_number', '__class__']
        self.assertEqual(set(model_dict.keys()), set(expected_keys))

        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(type(model_dict['created_at']), str)
        self.assertEqual(type(model_dict['updated_at']), str)

    def test_init_from_dict(self):
        """This method test initializing a new BaseModel instance from a dictionary."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        model_dict = my_model.to_dict()
        new_model = BaseModel(**model_dict)

        self.assertEqual(new_model.id, my_model.id)
        self.assertEqual(new_model.name, my_model.name)
        self.assertEqual(new_model.my_number, my_model.my_number)
        self.assertEqual(new_model.created_at, my_model.created_at)
        self.assertEqual(new_model.updated_at, my_model.updated_at)

    def test_str_representation(self):
        """This method test the string representation of BaseModel."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        str_repr = str(my_model)
        self.assertIn("[BaseModel]", str_repr)
        self.assertIn(my_model.id, str_repr)
        self.assertIn(my_model.name, str_repr)
        self.assertIn(str(my_model.my_number), str_repr)

if __name__ == '__main__':
    unittest.main()

