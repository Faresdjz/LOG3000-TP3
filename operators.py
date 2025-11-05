"""
Module contenant les opérateurs arithmétiques de base pour la calculatrice.

Ce module fournit les fonctions pour effectuer les quatre opérations arithmétiques
fondamentales : addition, soustraction, multiplication et division.
"""

def add(a,b):
    """
    Effectue l'addition de deux nombres.
    
    Args:
        a (float): Premier opérande
        b (float): Deuxième opérande
    
    Returns:
        float: La somme de a et b
    """
    return a + b

def subtract(a,b):
    """
    Effectue la soustraction de deux nombres.
    
    Args:
        a (float): Premier opérande
        b (float): Deuxième opérande
    
    Returns:
        float: La différence de a et b (a - b)
    """
    return a - b

def multiply(a,b):
    """
    Effectue la multiplication de deux nombres.
    
    Args:
        a (float): Premier opérande
        b (float): Deuxième opérande
    
    Returns:
        float: Le produit de a et b
    """
    return a * b

def divide(a,b):
    """
    Effectue la division de deux nombres.
    
    Args:
        a (float): Premier opérande (dividende)
        b (float): Deuxième opérande (diviseur)
    
    Returns:
        float: Le quotient de a divisé par b
    """
    return a / b
