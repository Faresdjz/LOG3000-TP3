# Module de Tests

## Raison d'être

Le répertoire `tests/` contient tous les tests unitaires et d'intégration pour l'application calculatrice Flask. Ces tests permettent de :

- ✅ Vérifier que les fonctionnalités fonctionnent correctement
- ✅ Détecter les bugs avant qu'ils n'atteignent la production
- ✅ Documenter le comportement attendu du code
- ✅ Faciliter la maintenance et les refactorisations

## Structure des tests

```
tests/
├── __init__.py              # Fichier d'initialisation du package de tests
├── test_operators.py        # Tests unitaires pour les opérateurs arithmétiques
├── test_calculate.py        # Tests unitaires pour la fonction calculate()
├── test_app.py              # Tests d'intégration pour les routes Flask
└── README.md                # Ce fichier (documentation du module de tests)
```

## Couverture des tests

### `test_operators.py`

**Objectif** : Tester les fonctions arithmétiques de base (`add`, `subtract`, `multiply`, `divide`)

**Couverture** :
- ✅ Addition avec entiers, négatifs et décimaux
- ✅ Soustraction avec cas positifs et négatifs
- ✅ Multiplication avec zéro et nombres négatifs
- ✅ Division normale et division par zéro

**Fonctions de test** :
- `test_add()` : Tests pour la fonction `add()`
- `test_subtract()` : Tests pour la fonction `subtract()`
- `test_multiply()` : Tests pour la fonction `multiply()`
- `test_divide()` : Tests pour la fonction `divide()`

### `test_calculate.py`

**Objectif** : Tester la fonction `calculate()` qui parse et évalue les expressions

**Couverture** :
- ✅ Expressions valides avec tous les opérateurs (+, -, *, /)
- ✅ Gestion des espaces dans les expressions
- ✅ Support des nombres décimaux
- ✅ Expressions invalides (vide, plusieurs opérateurs, opérateur mal placé, opérandes non numériques)

**Fonctions de test** :
- `test_valid_expressions()` : Tests pour les expressions valides
- `test_invalid_expressions()` : Tests pour les expressions invalides

### `test_app.py`

**Objectif** : Tester l'application Flask au niveau des routes HTTP

**Couverture** :
- ✅ Requête GET sur la route principale
- ✅ Requête POST avec expressions valides
- ✅ Requête POST avec expressions invalides

**Fonctions de test** :
- `test_index_get()` : Test de la route GET
- `test_index_post_valid()` : Test POST avec expression valide
- `test_index_post_invalid()` : Test POST avec expression invalide

## Prérequis

### Installation de pytest

Avant d'exécuter les tests, vous devez installer `pytest` :

```bash
# Activer l'environnement virtuel (si ce n'est pas déjà fait)
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Installer pytest
pip install pytest
```

### Vérification de l'installation

Vérifiez que pytest est correctement installé :

```bash
pytest --version
```

Vous devriez voir la version de pytest s'afficher (ex: `pytest 8.4.0`).

## Exécution des tests

### Exécuter tous les tests

```bash
pytest
```

### Exécuter avec affichage détaillé

```bash
pytest -v
```

### Exécuter un fichier de test spécifique

```bash
# Tests des opérateurs
pytest tests/test_operators.py

# Tests de la fonction calculate
pytest tests/test_calculate.py

# Tests de l'application Flask
pytest tests/test_app.py
```

### Exécuter un test spécifique

```bash
# Test spécifique
pytest tests/test_operators.py::test_add
```

### Exécuter avec affichage des print statements

```bash
pytest -s
```

### Exécuter et arrêter au premier échec

```bash
pytest -x
```

## Couverture de code

### Installation de pytest-cov

```bash
pip install pytest-cov
```

### Exécuter avec couverture

```bash
# Couverture pour tous les modules
pytest --cov=app --cov=operators

# Couverture avec rapport HTML
pytest --cov=app --cov=operators --cov-report=html
```

Le rapport HTML sera généré dans `htmlcov/index.html`.

## Interprétation des résultats

### Tests réussis

Lorsque tous les tests passent, vous verrez :

```
======================== test session starts ========================
collected 10 items

tests/test_operators.py ....                                    [ 40%]
tests/test_calculate.py ..                                       [ 60%]
tests/test_app.py ...                                            [100%]

======================= 10 passed in 0.25s ========================
```

### Tests échoués

Lorsqu'un test échoue, pytest affiche des informations détaillées :

```
FAILED tests/test_operators.py::test_subtract
================================ FAILURES ================================
AssertionError: assert -2 == 2
```

Cette sortie indique quel test a échoué et quelle assertion a échoué.

## Écrire de nouveaux tests

### Structure d'un test

```python
def test_nom_du_test():
    """Description du test."""
    assert fonction_testee(5, 3) == 8
```

### Bonnes pratiques

1. **Nommage** : Utilisez des noms descriptifs (`test_add`, `test_invalid_expression`)
2. **Un seul concept par test** : Chaque test doit vérifier une seule chose
3. **Docstrings** : Ajoutez une docstring courte expliquant le but du test
4. **Indépendance** : Les tests doivent être indépendants

### Exemple : Ajouter un test

```python
def test_nouvelle_fonctionnalite():
    """Teste la nouvelle fonctionnalité."""
    assert nouvelle_fonction(5) == 10
```

## Notes importantes

- Les tests utilisent `pytest.approx()` pour comparer les nombres flottants
- Les tests d'intégration Flask utilisent `app.test_client()` pour simuler des requêtes HTTP
- Les tests sont conçus pour être rapides et indépendants
- Tous les tests doivent passer avant de faire un commit ou une pull request

## Pour les nouveaux développeurs

1. **Commencer par lire les tests** : Les tests servent aussi de documentation
2. **Exécuter les tests avant de modifier le code** : Assurez-vous que tout fonctionne
3. **Exécuter les tests après vos modifications** : Vérifiez que vous n'avez rien cassé
4. **Ajouter des tests pour les nouvelles fonctionnalités** : Maintenez la couverture de code

## Ressources

- [Documentation pytest](https://docs.pytest.org/)
- [Testing Flask applications](https://flask.palletsprojects.com/en/2.3.x/testing/)

---

**Module de tests - TP3-LOG3000**

*Dernière mise à jour : Novembre 2024*
