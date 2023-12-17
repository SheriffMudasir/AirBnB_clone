#!/usr/bin/python3
"""This module create an instance of FileStorage"""

from models.engine.file_storage import FileStorage
from models.user import User
storage = FileStorage()
storage.reload()
