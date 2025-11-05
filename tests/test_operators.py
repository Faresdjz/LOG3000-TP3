"""
Tests unitaires pour le module operators.py.
"""

import pytest
from operators import add, subtract, multiply, divide


def test_add():
    """Teste l'addition."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(2.5, 1.5) == 4.0


def test_subtract():
    """Teste la soustraction."""
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(5.5, 2.3) == pytest.approx(3.2)


def test_multiply():
    """Teste la multiplication."""
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6


def test_divide():
    """Teste la division."""
    assert divide(10, 2) == 5.0
    assert divide(5, 2) == 2.5
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
