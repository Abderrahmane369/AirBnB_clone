#!/usr/bin/python3
"""Modules"""
import unittest
from models.base_model import BaseModel
from io import StringIO
import datetime

class TestBaseModel(unittest.TestCase):
    """Tests begins..."""
    def test_id(self):
        base = BaseModel()
        self.assertEqual(type(base.id), str)
        self.assertRegex(base.id, r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')

    def test_created_updated_at(self):
        base = BaseModel()
        self.assertEqual(type(base.created_at), datetime.datetime)
        self.assertEqual(type(base.updated_at), datetime.datetime)

        self.assertRegex(base.created_at.isoformat(), r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$')
        self.assertRegex(base.updated_at.isoformat(), r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$')

    def test_str(self):
        base = BaseModel()
        base.name = "AOAOAO"
        base.my_number = 23

        with StringIO() as buffer:
            import sys
            sys.stdout = buffer

            print(base)

            sys.stdout = sys.__stdout__

            printed_output = buffer.getvalue().strip()

        self.assertEqual(printed_output, f"[BaseModel] ({base.id}) {base.__dict__}")

    def test_save(self):
        base = BaseModel()

        base.save()

        self.assertRegex(base.updated_at.isoformat(), r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$')

    def test_to_dcit(self):
        base = BaseModel()
        base.name = "AOAOAO"
        base.my_number = 23

        base_ = {'my_number': 23, 'name': 'AOAOAO', '__class__': 'BaseModel', 'updated_at': base.updated_at.isoformat(), 'id': base.id, 'created_at': base.created_at.isoformat()}
        self.assertEqual(base.to_dict(), base_)
