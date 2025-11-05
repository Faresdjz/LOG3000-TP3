"""
Tests unitaires pour la fonction calculate().
"""

import pytest
from app import calculate


def test_valid_expressions():
    """Teste les expressions valides."""
    assert calculate("5 + 3") == 8
    assert calculate("10 - 4") == 6
    assert calculate("2 * 3") == 6
    assert calculate("10 / 2") == 5.0
    assert calculate("5/2") == 2.5
    assert calculate("  5 + 3  ") == 8


def test_invalid_expressions():
    """Teste les expressions invalides."""
    with pytest.raises(ValueError, match="empty expression"):
        calculate("")
    
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("   ")
    
    with pytest.raises(ValueError, match="only one operator is allowed"):
        calculate("5 + 3 + 2")
    
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("5 +")
    
    with pytest.raises(ValueError, match="operands must be numbers"):
        calculate("abc + 5")


def test_mixed_spaces_and_variants():
    """Espaces variés et variantes d'opérateurs."""
    assert calculate("5  +   3") == 8
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("+5")
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("5+")
    with pytest.raises(ValueError, match="only one operator is allowed"):
        calculate("5+-3")


def test_non_string_inputs():
    """Entrées non-string rejetées."""
    with pytest.raises(ValueError, match="empty expression"):
        calculate(123)
    with pytest.raises(ValueError, match="empty expression"):
        calculate([])
    with pytest.raises(ValueError, match="empty expression"):
        calculate({})
