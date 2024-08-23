# Copyright (c) 2024 Pritilata Saha
#
# This software is released under the MIT License.
# See the LICENSE file for details.
#
# SPDX-License-Identifier: MIT

# tests/test_arithmetic.py

import unittest
from calculator import add, subtract, multiply, divide


class TestArithmetic(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
