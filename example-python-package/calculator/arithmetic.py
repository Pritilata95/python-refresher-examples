# Copyright (c) 2024 Pritilata Saha
#
# This software is released under the MIT License.
# See the LICENSE file for details.
#
# SPDX-License-Identifier: MIT

# calculator/arithmetic.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot be divided by Zero. Please enter a non-zero value.")
    return a / b
