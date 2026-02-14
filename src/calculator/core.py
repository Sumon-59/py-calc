"""
Core calculation functions.

This module contains basic arithmetic operations used by CLI and API.
"""


def add(a: float, b: float) -> float:
    """Return addition of two numbers."""
    return a + b


def sub(a: float, b: float) -> float:
    """Return subtraction of two numbers."""
    return a - b


def mul(a: float, b: float) -> float:
    """Return multiplication of two numbers."""
    return a * b


def div(a: float, b: float) -> float:
    """
    Return division of two numbers.

    Raises:
        ValueError: if division by zero.
    """

    if b == 0:
        raise ValueError("Cannot Divide by zero")
    return a / b
