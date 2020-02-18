#!/usr/bin/python3
"""
Defines class User
"""
from models.base_models import BaseModel


class User(BaseModel):
    """Defines class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
