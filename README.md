# 🧮 Calculatrice Web Flask

Une application web de calculatrice simple et moderne développée avec Flask, permettant d'effectuer des opérations arithmétiques de base via une interface utilisateur intuitive.

## 📋 Table des matières

- [À propos](#à-propos)
- [Fonctionnalités](#fonctionnalités)
- [Technologies utilisées](#technologies-utilisées)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du projet](#structure-du-projet)
- [Tests](#tests)
- [Contribution](#contribution)
- [Équipe](#équipe)
- [Licence](#licence)

## 🎯 À propos

### But du projet

Ce projet est une **calculatrice web interactive** développée dans le cadre du cours LOG3000. L'application permet aux utilisateurs d'effectuer des opérations arithmétiques de base (addition, soustraction, multiplication, division) via une interface web moderne et responsive.

### Portée du projet

L'application est conçue pour :
- ✅ Fournir une interface utilisateur simple et intuitive pour les calculs arithmétiques
- ✅ Valider et traiter les expressions mathématiques de la forme "nombre opérateur nombre"
- ✅ Gérer les erreurs de manière élégante et informer l'utilisateur
- ✅ Servir de base pédagogique pour l'apprentissage de Flask, Git, et des bonnes pratiques de développement
- ✅ Démonstrer la structure d'un projet web Python professionnel

### Limitations actuelles

- Une seule opération à la fois (format : `nombre1 opérateur nombre2`)
- Opérations arithmétiques de base uniquement (+, -, *, /)
- Pas de support pour les parenthèses ou expressions complexes
- Pas de gestion de l'historique des calculs

## ✨ Fonctionnalités

- **Interface web moderne** : Design sombre et épuré avec feedback visuel
- **Opérations arithmétiques** : Addition (+), Soustraction (-), Multiplication (*), Division (/)
- **Validation des expressions** : Vérification du format et gestion des erreurs
- **Feedback utilisateur** : Messages d'erreur clairs en cas de problème
- **Interface responsive** : Adaptation à différentes tailles d'écran
- **Calcul en temps réel** : Évaluation des expressions via requête POST au serveur

## 🛠 Technologies utilisées

- **Python 3.x** : Langage de programmation principal
- **Flask** : Framework web léger pour Python
- **Jinja2** : Moteur de templates (intégré à Flask)
- **HTML5** : Structure de l'interface utilisateur
- **CSS3** : Styling et design moderne (Grid, transitions)
- **JavaScript** : Interactivité côté client pour la saisie

## 📦 Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Python 3.7 ou supérieur** (recommandé : Python 3.9+)
  - Vérifiez avec : `python --version` ou `python3 --version`
- **pip** (gestionnaire de paquets Python, généralement inclus avec Python)
  - Vérifiez avec : `pip --version` ou `pip3 --version`
- **Git** (pour cloner le dépôt)
  - Vérifiez avec : `git --version`
- **Navigateur web moderne** (Chrome, Firefox, Edge, Safari)
- **IDE ou éditeur de texte** (VS Code, PyCharm, Sublime Text, etc.)

## 🚀 Installation

Suivez ces étapes pour installer et configurer l'application sur votre machine locale.

### Étape 1 : Cloner le dépôt

```bash
git clone <url-du-depot>
cd TP3-LOG3000
```

**Note** : Remplacez `<url-du-depot>` par l'URL réelle du dépôt Git.

### Étape 2 : Créer un environnement virtuel (recommandé)

Créer un environnement virtuel isole les dépendances du projet et évite les conflits avec d'autres projets Python.

```bash
# Créer l'environnement virtuel
python -m venv venv

# Ou avec python3 sur certains systèmes
python3 -m venv venv
```

### Étape 3 : Activer l'environnement virtuel

**Sur Windows :**
```bash
venv\Scripts\activate
```

**Sur macOS/Linux :**
```bash
source venv/bin/activate
```

**Indication de succès** : Vous devriez voir `(venv)` au début de votre ligne de commande.

### Étape 4 : Installer les dépendances

```bash
pip install flask
```

**Alternative** : Si vous utilisez `pip3` :
```bash
pip3 install flask
```

### Étape 5 : Vérifier l'installation

Vérifiez que Flask est correctement installé :
```bash
python -c "import flask; print(flask.__version__)"
```

Vous devriez voir la version de Flask s'afficher (ex: `2.3.0`).

## 💻 Utilisation

### Démarrer l'application

1. **Activer l'environnement virtuel** (si ce n'est pas déjà fait)
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

2. **Lancer l'application Flask**
   ```bash
   python app.py
   ```

   **Note** : Sur certains systèmes, utilisez `python3 app.py`

3. **Vérifier que le serveur démarre**
   ```
   * Running on http://127.0.0.1:5000
   * Debug mode: on
   ```

### Accéder à l'application

1. Ouvrez votre navigateur web
2. Naviguez vers : **`http://localhost:5000`** ou **`http://127.0.0.1:5000`**
3. L'interface de la calculatrice devrait s'afficher

### Utiliser la calculatrice

#### Interface utilisateur

L'interface comprend :
- **Champ d'affichage** : Affiche l'expression en cours et le résultat
- **Boutons numériques** : Chiffres 0-9 pour construire les nombres
- **Boutons opérateurs** : +, -, *, / pour les opérations
- **Bouton Clear (C)** : Efface complètement l'affichage
- **Bouton Égal (=)** : Calcule et affiche le résultat

#### Format d'expression

L'application accepte des expressions de la forme :
```
nombre1 opérateur nombre2
```

**Exemples valides :**
- `5 + 3` → Résultat : `8`
- `10 - 4` → Résultat : `6`
- `2 * 7` → Résultat : `14`
- `15 / 3` → Résultat : `5`
- `3.5 + 2.1` → Résultat : `5.6`

**Notes importantes :**
- Les espaces sont automatiquement supprimés
- Un seul opérateur est autorisé par expression
- Les nombres décimaux sont supportés (utilisez le point `.`)
- Le format doit être strictement : nombre → opérateur → nombre

#### Exemples d'utilisation

1. **Calcul simple** :
   - Cliquez sur `5`, puis `+`, puis `3`, puis `=`
   - Résultat affiché : `8`

2. **Calcul avec décimal** :
   - Cliquez sur `1`, `.`, `5`, puis `*`, puis `2`, puis `=`
   - Résultat affiché : `3.0`

3. **Effacer** :
   - Cliquez sur `C` pour effacer l'affichage et recommencer

#### Gestion des erreurs

L'application affiche des messages d'erreur clairs dans les cas suivants :
- **Expression vide** : `Error: empty expression`
- **Plusieurs opérateurs** : `Error: only one operator is allowed`
- **Format invalide** : `Error: invalid expression format`
- **Opérandes non numériques** : `Error: operands must be numbers`

### Arrêter l'application

Dans le terminal où l'application tourne, appuyez sur **`Ctrl + C`** pour arrêter le serveur.

### Désactiver l'environnement virtuel

Une fois terminé, vous pouvez désactiver l'environnement virtuel :
```bash
deactivate
```

## 📁 Structure du projet

```
TP3-LOG3000/
├── app.py                 # Application Flask principale (routes, logique métier)
├── operators.py           # Module des opérateurs arithmétiques (add, subtract, multiply, divide)
├── README.md              # Documentation principale du projet (ce fichier)
├── .gitignore             # Fichiers à ignorer par Git
├── templates/             # Templates HTML (Jinja2)
│   ├── index.html         # Interface utilisateur de la calculatrice
│   └── README.md          # Documentation du module templates
├── static/                # Fichiers statiques (CSS, images, JS)
│   ├── style.css          # Feuille de style pour l'interface
│   └── README.md          # Documentation du module static
└── __pycache__/           # Fichiers Python compilés (générés automatiquement, ignoré par Git)
```

### Description des fichiers principaux

- **`app.py`** : Point d'entrée de l'application Flask
  - Définit la route principale `/`
  - Contient la fonction `calculate()` pour évaluer les expressions
  - Gère les requêtes GET (affichage) et POST (calcul)

- **`operators.py`** : Module des opérations arithmétiques
  - Fonctions : `add()`, `subtract()`, `multiply()`, `divide()`
  - Chaque fonction prend deux opérandes et retourne le résultat

- **`templates/index.html`** : Interface utilisateur
  - Formulaire HTML avec boutons interactifs
  - Scripts JavaScript pour la gestion de l'affichage
  - Utilise Jinja2 pour l'injection de variables

- **`static/style.css`** : Styles visuels
  - Design sombre et moderne
  - Layout en grille CSS pour les boutons
  - Effets de survol et transitions

Pour plus de détails, consultez les fichiers `README.md` dans les répertoires `templates/` et `static/`.

## 🧪 Tests

### Structure des tests

Les tests sont organisés dans un répertoire `tests/` avec la structure suivante :
```
tests/
├── __init__.py
├── test_operators.py      # Tests unitaires pour les opérateurs
├── test_calculate.py      # Tests pour la fonction calculate()
└── test_app.py            # Tests d'intégration pour les routes Flask
```

### Exécuter les tests

Utilisez `pytest` pour exécuter les tests :

```bash
# Installer pytest (si ce n'est pas déjà fait)
pip install pytest

# Exécuter tous les tests
pytest

# Exécuter avec affichage détaillé
pytest -v

# Exécuter un fichier de test spécifique
pytest tests/test_operators.py

# Exécuter avec couverture de code
pip install pytest-cov
pytest --cov=app --cov=operators
```

### Écrire des tests

Pour ajouter de nouveaux tests :
1. Créez un fichier dans `tests/` avec le préfixe `test_`
2. Utilisez les assertions `assert` pour vérifier les résultats
3. Suivez les conventions de nommage : `test_nom_de_la_fonction()`

**Exemple de test** :
```python
def test_add():
    from operators import add
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

## 🤝 Contribution

Ce projet suit un workflow Git standard pour faciliter la collaboration et maintenir la qualité du code.

### Workflow de développement

1. **Créer une branche** pour votre fonctionnalité ou correction
   ```bash
   git checkout -b feature/nom-de-la-fonctionnalite
   # ou
   git checkout -b fix/nom-du-bug
   ```

2. **Faire vos modifications** et commiter régulièrement
   ```bash
   git add .
   git commit -m "Description claire des changements"
   ```

3. **Pousser votre branche** vers le dépôt distant
   ```bash
   git push origin feature/nom-de-la-fonctionnalite
   ```

4. **Créer une Pull Request (PR)** sur la plateforme Git (GitHub, GitLab, etc.)
   - Titre descriptif et clair
   - Description détaillée des changements
   - Référence aux issues liées (si applicable)

### Conventions de branches

- **`main`** ou **`master`** : Branche principale (code stable)
- **`feature/...`** : Nouvelles fonctionnalités
- **`fix/...`** : Corrections de bugs
- **`docs/...`** : Améliorations de la documentation
- **`refactor/...`** : Refactorisation du code

### Standards de code

- **Docstrings** : Toutes les fonctions et classes doivent avoir des docstrings
- **Commentaires** : Commentaires utiles expliquant le "pourquoi", pas seulement le "quoi"
- **Nommage** : Noms de variables et fonctions clairs et descriptifs
- **Formatage** : Respecter PEP 8 (style guide Python)
- **Tests** : Ajouter des tests pour les nouvelles fonctionnalités

### Créer une Pull Request

Lors de la création d'une PR, inclure :
1. **Titre** : Description concise des changements
2. **Description** : 
   - Ce qui a été modifié et pourquoi
   - Comment tester les changements
   - Screenshots (si changement d'interface)
3. **Checklist** :
   - [ ] Code testé localement
   - [ ] Documentation mise à jour
   - [ ] Pas de nouveaux warnings
   - [ ] Tests passent

### Signaler un problème (Issue)

Pour signaler un bug ou proposer une fonctionnalité :
1. Vérifiez que l'issue n'existe pas déjà
2. Créez une nouvelle issue avec :
   - **Titre** clair et descriptif
   - **Description** détaillée du problème ou de la fonctionnalité
   - **Étapes pour reproduire** (pour les bugs)
   - **Comportement attendu** vs **comportement actuel**

### Processus de review

1. Les PR sont revues par au moins un membre de l'équipe
2. Les commentaires doivent être adressés avant le merge
3. Les tests doivent passer avant le merge
4. Le code doit respecter les standards établis

## 👥 Équipe

**Groupe 02 - Équipe 24**

- **Akram Lourhmati** - 2287991
- **Zine-Eddine Mellata** - 2293672
- **Fares Laadjel** - 2297799

## 📝 Notes importantes

- **Mode développement** : L'application fonctionne en mode debug (`debug=True`) pour faciliter le développement
- **Production** : Pour déployer en production, désactivez le mode debug dans `app.py` et utilisez un serveur WSGI approprié (ex: Gunicorn)
- **Port** : Le serveur écoute sur le port 5000 par défaut. Si ce port est occupé, modifiez-le dans `app.py` :
  ```python
  app.run(debug=True, port=5001)  # Changer 5001 par le port désiré
  ```

## 📚 Ressources supplémentaires

- [Documentation Flask](https://flask.palletsprojects.com/)
- [Documentation Jinja2](https://jinja.palletsprojects.com/)
- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Guide de contribution GitHub](https://github.com/docs/contributing)



---

**Projet réalisé dans le cadre du cours LOG3000 - École Polytechnique de Montréal**

*Dernière mise à jour : Novembre 2024*
