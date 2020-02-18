#!/usr/bin/python3
""" Test for base_models class"""

import unittest
from datetime import date, time, datetime
import uuid
from models import storage
from models.base_model import BaseModel
import os
import time
import pep8


class TestBaseModel(unittest.TestCase):
    """ Test For base_model class"""

    def setUp(self):
        """ Move Json files if they exist """
        if os.path.isfile("file.json"):
            os.rename("file.json", "file.json.temp")

    def tearDown(self):
        """ Delete test files and put original files back"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("file.json.temp"):
            os.rename("file.json.temp", "file.json")

    def test_pep8(self):
        """ checks for pep8 compliance """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_file(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors and warnings")

    def test_type(self):
        """ check name, number, class, updated_at, created_at, id type test """
        a = BaseModel()
        self.assertTrue(type(a), BaseModel)
        a.name = "Toxic_player"
        self.assertEqual(a.name, "Toxic_player")
        self.assertTrue(type(a.name), str)
        a.my_number = 5
        self.assertEqual(a.my_number, 5)
        self.assertTrue(type(a.my_number), int)
        self.assertEqual(type(a.id), str)
        self.assertEqual(type(a.created_at), datetime)
        self.assertEqual(type(a.updated_at), datetime)

    def test_defaultAttribute(self):
        """ check for id, created_at, updated_at default attributes """
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_Extra(self):
        """ check for the dictionary """
        c = BaseModel()
        c.birthday = [12, 12, 2012]
        c.dictionary = {day: "12", month: "12", year: "2012"}
        self.assertTrue(hasattr(c, "birthday"))
        self.assertEqual(type(c.birthday), list)
        self.assertTrue(hasattr(c, "dictionary"))
        self.assertEqual(type(c.dictionary), dict)

    def test_different_id(self):
        """ Id should be different """
        d = BaseModel()
        e = BaseModel()
        self.assertNotEqual(e.id, d.id)
        self.assertEqual(len(e.id), len(d.id))

    def test_save(self):
        """ checks if updated_at is saved """
        f = BaseModel()
        g = f.updated_at
        time.sleep(0.1)
        f.save()
        h = f.updated_at
        self.assertNotEqual(g, h)

    def test_to_dict(self):
        """ dictionary conversion test """
        i = BaseModel()
        i.name = "Cute_anime_girl"
        i.number = 25
        j = i.to_dict()
        k = ["id", "name", "my_number", "created_at", "updated_at",
             "__class__"]
        self.assertEqual(j["name"], "Cute_anime_girl")
        self.assertEqual(j["my_number"], 25)
        self.assertEqual(j["__class__"], "BaseModel")
        self.assertCountEqual(j.keys(), k)

    def test_to_dict_attributes(self):
        """ check Created_at and Updated_at values"""
        l = BaseModel()
        m = "%Y-%m-%dT%H:%M:%S.%f"
        n = l.to_dict()
        self.assertEqual(n["created_at"], l.created_at.strftime(m))
        self.assertEqual(n["updated_at"], l.updated_at.strftime(m))
        self.assertEqual(n["__class__"], "BaseModel")
        self.assertEqual(type(n["created_at"]), str)
        self.assertEqual(type(n["updated_at"]), str)

    def test_kwarg_nameError(self):
        """ check for kwargs syntax """
        with self.assertRaises(NameError):
            o = BaseModel(**o)

    def test_kwargs_typeError(self):
        """check for kwargs syntax """
        with self.assertRaises(TypeError):
            p = BaseModel(**"p")

    def test_kwargs_nameError(self):
        """check for kwargs syntax """
        with self.assertRaises(NameError):
            q = BaseModel(**{q})

    def test_kwargs_typeError(self):
        """ check for kwargs syntax """
        with self.assertRaises(TypeError):
            r = BaseModel(**{"r"})

    def test_intAttribute(self):
        """ int attribute """
        s = BaseModel(1, 2, 3, 4)
        self.assertTrue(hasattr(s, "id"))
        self.assertTrue(hasattr(s, "created_at"))
        self.assertTrue(hasattr(s, "updated_at"))

    def test_nanAttribute(self):
        """ nan attribute """
        t = BaseModel(float("nan"))
        self.assertTrue(hasattr(t, "id"))
        self.assertTrue(hasattr(t, "created_at"))
        self.assertTrue(hasattr(t, "updated_at"))

    def test_infAttribute(self):
        """ infinite attribute """
        u = BaseModel(float("inf"))
        self.assertTrue(hasattr(u, "id"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))

    def test_noneAttribute(self):
        """ None Attribute """
        v = BaseModel(None)
        self.assertTrue(hasattr(v, "id"))
        self.assertTrue(hasattr(v, "created_at"))
        self.assertTrue(hasattr(v, "updated_at"))

if __name__ == '__main__':
    unittest.main()
