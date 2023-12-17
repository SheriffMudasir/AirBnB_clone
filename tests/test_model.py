#!/usr/bin/python3
"""
This module is a unittests for the State, City, Amenity, Place, and Review classes in the AirBnB Clone

"""

import unittest
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime
from models.base_model import BaseModel


class TestModels(unittest.TestCase):
    """This class test case class for the State, City, Amenity, Place, and Review classes."""

    def test_state(self):
        """This method test the State class."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
        self.assertEqual(state.name, "")
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)

    def test_city(self):
        """This method test the City class."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_amenity(self):
        """This method test the Amenity class."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)
        self.assertEqual(amenity.name, "")
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_place(self):
        """This method test the Place class."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)

    def test_review(self):
        """This method test the Review class."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()

