#!/usr/bin/python4
"""__Modules__"""
import json
from models.base_model import BaseModel


class FileStorage:
    """File Storage Class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects.update(
            {f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fjson:
            json.dump({k: v.to_dict()
                      for k, v in FileStorage.__objects.items()}, fjson)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as fjson:
                items_ = json.load(fjson).items()
                FileStorage.__objects.update(
                    {k: eval(v['__class__'])(**v) for k, v in items_})

        except FileNotFoundError:
            pass