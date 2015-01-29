import os
from unittest import TestCase
from plugins.coffee import CoffeePlugin

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class TestSafeCall(TestCase):
    def setUp(self):
        self.plugin = CoffeePlugin()

    def test_image_path(self):
        self.assertEqual(os.path.abspath('../plugins/coffee/resources/two_coffee.jpg'), self.plugin.get_image_path)
