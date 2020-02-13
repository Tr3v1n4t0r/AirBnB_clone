#!/usr/bin/python3

import uuid
from datetime import date datetime time

class BaseModel:
    def __init__(self, id, save, to_dict, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.save = save
        self.to_dict =
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

