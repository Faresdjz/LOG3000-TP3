"""
Tests d'intégration pour l'application Flask.
"""

import pytest
from app import app


def test_index_get():
    """Teste la requête GET."""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Flask Calculator' in response.data


def test_index_post_valid():
    """Teste la requête POST avec expression valide."""
    client = app.test_client()
    response = client.post('/', data={'display': '5 + 3'})
    assert response.status_code == 200
    assert b'8' in response.data


def test_index_post_invalid():
    """Teste la requête POST avec expression invalide."""
    client = app.test_client()
    response = client.post('/', data={'display': 'invalid'})
    assert response.status_code == 200
    assert b'Error' in response.data


def test_index_post_subtraction():
    """Soumission POST d'une soustraction (-)."""
    client = app.test_client()
    response = client.post('/', data={'display': '10 - 4'})
    assert response.status_code == 200
    assert b'6' in response.data


def test_index_post_multiplication():
    """Soumission POST d'une multiplication (*)."""
    client = app.test_client()
    response = client.post('/', data={'display': '3 * 4'})
    assert response.status_code == 200
    assert b'12' in response.data


def test_index_post_division():
    """Soumission POST d'une division (/)."""
    client = app.test_client()
    response = client.post('/', data={'display': '15 / 3'})
    assert response.status_code == 200
    assert b'5' in response.data
