#!/usr/bin/python3
"""Modules"""
from .engine import file_storage as fs

storage = fs.FileStorage()
storage.reload()
