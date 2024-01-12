from django.test import SimpleTestCase
from app import calc
class AdditionClass(SimpleTestCase):
    def test_add_number(self):
        """ Test the addition of two positive numbers"""
        rel = calc.add(2,3)
        self.assertEqual(rel, 7)