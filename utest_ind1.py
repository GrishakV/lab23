#!/usr/bin/env python3
# -*- config: utf-8 -*-

import unittest
import sqlite3
import indmodule

db = sqlite3.connect('ind_utest.sqlite')
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS peoples (
            _id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            day INTEGER,
            month INTEGER,
            year INTEGER
        )''')

cur.execute('''INSERT INTO peoples (
                name, phone, day, month, year) VALUES (?, ?, ?, ?, ?)
                ''', ('test1', 11111, 14, 12, 1998))
db.commit()

class PeopleTest(unittest.TestCase):
    """People tests"""

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("setUpClass")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("tearDownClass")

    def setUp(self):
        """Set up for test"""
        print("Set up for [" + self.shortDescription() + "]")

    def tearDown(self):
        """Tear down for test"""
        print("Tear down for [" + self.shortDescription() + "]")
        print("")

    def test_select(self):
        """Select operation test"""
        print("id: " + self.id())
        people = indmodule.People()
        people.load()
        sel_test_v = people.select(12)
        res = ''
        if sel_test_v:
            for person in sel_test_v:
                res = person.name
        self.assertEqual(res, 'test1')


if __name__ == '__main__':
    unittest.main()
