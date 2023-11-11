#!/usr/bin/python3
"""Modules"""
import unittest
from models.engine.file_storage import FileStorage
from models import storage
import os
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Let's test"""

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_reload_save(self):
        base = BaseModel()
        base.name = 'NAME'
        base.number = 111

        base.save()

        storage.reload()

        abase = storage.all()[f"BaseModel.{base.id}"]

        self.assertEqual(abase.to_dict(), base.to_dict())

    def test_reload_save_Alot(self):
        base = BaseModel()
        base.name = 'A'
        base.number = 1

        base1 = BaseModel()
        base.name = 'B'
        base.number = 2

        base2 = BaseModel()
        base.name = 'C'
        base.number = 3

        base.save()
        base1.save()
        base2.save()

        storage.reload()

        abase = storage.all()

        self.assertEqual(abase[f"BaseModel.{base.id}"].to_dict(),
                         base.to_dict())
        self.assertEqual(abase[f"BaseModel.{base1.id}"].to_dict(),
                         base1.to_dict())
        self.assertEqual(abase[f"BaseModel.{base2.id}"].to_dict(),
                         base2.to_dict())

    def test_fileNotFound(self):
        base = BaseModel()
        base.name = 'A'
        base.number = 1

        abase = storage.all()

        self.assertEqual(abase, {})
