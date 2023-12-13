import unittest
from models import storage
from models.base_model import BaseModel
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.command = HBNBCommand()
        self.storage = storage

    def test_do_create_empty_line(self):
        """This method Test `do_create` with empty line"""
        result = self.command.do_create("")
        self.assertEqual(result, "** class name missing **")

    def test_do_create_valid_class(self):
        """This method Test `do_create` with valid class"""
        instance = BaseModel()
        self.command.do_create("BaseModel")
        self.assertIn(instance.id, self.storage.all())

    def test_do_create_invalid_class(self):
        """This method Test `do_create` with invalid class"""
        result = self.command.do_create("InvalidClass")
        self.assertEqual(result, "** class doesn't exist **")

    def test_do_show_empty_line(self):
        """This method Test `do_show` with empty line"""
        result = self.command.do_show("")
        self.assertEqual(result, "** class name missing **")

    def test_do_show_missing_instance_id(self):
        """This method Test `do_show` with missing instance id"""
        result = self.command.do_show("BaseModel")
        self.assertEqual(result, "** instance id missing **")

    def test_do_show_invalid_class(self):
        """This method Test `do_show` with invalid class"""
        result = self.command.do_show("InvalidClass 123")
        self.assertEqual(result, "** class doesn't exist **")

    def test_do_show_nonexistent_instance(self):
        """ This method Test `do_show` with nonexistent instance"""
        result = self.command.do_show("BaseModel nonexisting_id")
        self.assertEqual(result, "** no instance found **")

    def test_do_show_valid_instance(self):
        """This method Test `do_show` with valid instance"""
        instance = BaseModel()
        self.storage.all()[
            f"{instance.__class__.__name__}.{instance.id}"] = instance
        result = self.command.do_show(
            f"{instance.__class__.__name__} {instance.id}")
        self.assertEqual(result, str(instance))

    def test_do_destroy_empty_line(self):
        """This method Test `do_destroy` with empty line"""
        result = self.command.do_destroy("")
        self.assertEqual(result, "** class name missing **")

    def test_do_destroy_missing_instance_id(self):
        """ This method Test `do_destroy` with missing instance id"""
        result = self.command.do_destroy("BaseModel")
        self.assertEqual(result, "** instance id missing **")

    def test_do_destroy_invalid_class(self):
        """This method Test `do_destroy` with invalid class"""
        result = self.command.do_destroy("InvalidClass 123")
        self.assertEqual(result, "** class doesn't exist **")

    def test_do_destroy_nonexistent_instance(self):
        """This method Test `do_destroy` with nonexistent instance"""
        result = self.command.do_destroy("BaseModel nonexisting_id")
        self.assertEqual(result, "** no instance found **")

    def test_do_destroy_valid_instance(self):
        """This method Test `do_destroy` with valid instance"""
        instance = BaseModel()
        self.storage.all()[
            f"{instance.__class__.__name__}.{instance.id}"] = instance
        self.command.do_destroy(f"{instance.__class__.__name__} {instance.id}")
        self.assertNotIn(instance.id, self.storage.all())

if __name__ == "__main__":
    unittest.main()
