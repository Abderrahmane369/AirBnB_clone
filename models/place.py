#!/usr/bin/python3
"""Modules"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class"""
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = int()
    number_bathrooms = int()
    max_guest = int()
    price_by_night = int()
    latitude = float()
    longitude = float()
    amenity_ids = []
