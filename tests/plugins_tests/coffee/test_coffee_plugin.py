import os
from unittest import TestCase
from plugins.coffee import CoffeePlugin

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class TestSafeCall(TestCase):
    def setUp(self):
        self.plugin = CoffeePlugin()

    def test_path_to_resource_directory(self):
        self.assertEqual(self.abspath_to_plugin_resources_directory, self.plugin.abspath_to_resources_directory)

    def test_path_to_coffee_directory(self):
        expected = os.path.join(self.abspath_to_plugin_resources_directory, self.plugin.two_coffee_directory)
        self.assertEqual(expected, self.plugin.abspath_to_coffee_directory)

    def test_path_to_tee_directory(self):
        expected = os.path.join(self.abspath_to_plugin_resources_directory, self.plugin.one_tea_directory)
        self.assertEqual(expected, self.plugin.abspath_to_tea_directory)

    @property
    def abspath_to_plugin_resources_directory(self):
        return os.path.join(self.abspath_to_plugin_directory, self.plugin.resources_directory)

    @property
    def abspath_to_plugin_directory(self):
        return os.path.abspath('../plugins/coffee')
