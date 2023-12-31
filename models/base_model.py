#!/usr/bin/python3
"""module documentation"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """BaseModel is the parent class"""

    def __init__(self, *args, **kwargs):
        """__init__ method (The constructor)"""
        if len(kwargs) != 0:
            self.__dict__.update(kwargs)

            if '__class__' in kwargs:
                del self.__dict__['__class__']

            if 'created_at' in self.__dict__:
                self.__dict__['created_at'] = datetime.fromisoformat(
                    self.__dict__['created_at'])
            if 'updated_at' in self.__dict__:
                self.__dict__['updated_at'] = datetime.fromisoformat(
                    self.__dict__['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """__str__ is a special method that provides a string representation
                of an object"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        """_dict = self.__dict__

        if 'created_at' in _dict and type(_dict['created_at']) != str:
            _dict['created_at'] = _dict['created_at'].isoformat()
        if 'updated_at' in _dict and type(_dict['updated_at']) != str:
            _dict['updated_at'] = _dict['updated_at'].isoformat()

        _dict['__class__'] = self.__class__.__name__"""
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

        # return _dict
