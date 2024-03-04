#!/usr/bin/env python3
"""
Unittest
"""
import unittest
import parameterized
from Unittests_and_integration_tests.utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ unittest """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == '__main__':
    unittest.main()
