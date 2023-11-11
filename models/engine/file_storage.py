#!/usr/bin/python4
"""__Modules__"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City


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
        cnmti = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'City': City, 'State': State, 'Amenity': Amenity
        }
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as fjson:
                items_ = json.load(fjson).items()
                FileStorage.__objects.update(
                    {k: cnmti[v['__class__']](**v) for k, v in items_})

        except FileNotFoundError:
            pass
