#!/usr/bin/python3
"""Modules"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Testing..."""

    def test_normal(self):
        user = User()
        user.name = "USER"
        user.number = 532
        user.email = "O"
        user.first_name = "US"
        user.last_name = "ER"
        user.password = "USER532"

        self.assertEqual(user.to_dict(), {'__class__': 'User', 'id': user.id,
                                          'name': 'USER', 'number': 532,
                                          'created_at': user.created_at,
                                          'updated_at': user.updated_at,
                                          'email': 'O',
                                          'first_name': 'US',
                                          'password': 'USER532'})
