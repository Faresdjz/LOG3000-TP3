# 🧮 Calculatrice Web Flask

Une application web de calculatrice simple développée avec Flask, conçue pour pratiquer les bonnes pratiques de gestion de dépôt Git et de développement collaboratif.

## 📋 Table des matières

- [À propos](#à-propos)
- [Fonctionnalités](#fonctionnalités)
- [Technologies utilisées](#technologies-utilisées)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du projet](#structure-du-projet)
- [Équipe](#équipe)
- [Objectifs pédagogiques](#objectifs-pédagogiques)

## 🎯 À propos

Ce projet est une calculatrice web interactive permettant d'effectuer des opérations arithmétiques de base (addition, soustraction, multiplication, division). L'objectif principal est de développer les compétences en gestion de dépôt Git, documentation de code, tests unitaires et adoption des bonnes pratiques de développement collaboratif.

## ✨ Fonctionnalités

- **Opérations arithmétiques** : Addition (+), Soustraction (-), Multiplication (*), Division (/)
- **Interface web intuitive** : Interface utilisateur moderne et responsive
- **Validation des expressions** : Gestion des erreurs et validation des entrées
- **Calcul en temps réel** : Evaluation des expressions mathématiques via requête POST

## 🛠 Technologies utilisées

- **Python 3** : Langage de programmation principal
- **Flask** : Framework web léger pour Python
- **HTML5** : Structure de l'interface utilisateur
- **CSS3** : Styling et design de l'interface
- **JavaScript** : Interactivité côté client

## 📦 Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Python 3.x** (version 3.7 ou supérieure recommandée)
- **pip** (gestionnaire de paquets Python)
- **Navigateur web moderne** (Chrome, Firefox, Edge, Safari)
- **IDE de votre choix** (VS Code, PyCharm, etc.)

## 🚀 Installation

1. **Cloner le dépôt** (ou télécharger le projet)
   ```bash
   git clone <url-du-depot>
   cd TP3-LOG3000
   ```

2. **Créer un environnement virtuel** (recommandé)
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**
   - Sur Windows :
     ```bash
     venv\Scripts\activate
     ```
   - Sur macOS/Linux :
     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances**
   ```bash
   pip install flask
   ```

## 💻 Utilisation

1. **Démarrer l'application**
   ```bash
   python app.py
   ```

2. **Accéder à l'application**
   - Ouvrez votre navigateur web
   - Naviguez vers : `http://localhost:5000`
   - L'interface de la calculatrice devrait s'afficher

3. **Utiliser la calculatrice**
   - Cliquez sur les boutons numériques et opérateurs pour construire votre expression
   - Cliquez sur `=` pour calculer le résultat
   - Cliquez sur `C` pour effacer l'affichage
   - Format d'expression : `nombre1 opérateur nombre2` (ex: `5+3`, `10/2`)

## 📁 Structure du projet

```
TP3-LOG3000/
├── app.py                 # Application Flask principale
├── operators.py           # Module contenant les fonctions d'opérations arithmétiques
├── README.md             # Documentation du projet
├── templates/
│   └── index.html        # Template HTML de l'interface
├── static/
│   └── style.css         # Feuille de style CSS
└── __pycache__/          # Fichiers Python compilés (générés automatiquement)
```

## 👥 Équipe

**Groupe 02 - Équipe 24**

- **Akram Lourhmati** - 2287991
- **Zine-Eddine Mellata** - 2293672
- **Fares Laadjel** - 2297799

## 🎓 Objectifs pédagogiques

Ce projet vise à développer les compétences suivantes :

- ✅ Gestion de dépôt Git (branches, merges, commits)
- ✅ Documentation de code et de projet
- ✅ Tests unitaires et validation
- ✅ Bonnes pratiques de développement collaboratif
- ✅ Structure de projet et organisation du code
- ✅ Développement web avec Flask

## 📝 Notes

- L'application fonctionne en mode debug pour le développement
- Pour la production, désactivez le mode debug dans `app.py`
- Assurez-vous que le port 5000 est disponible, sinon modifiez le port dans `app.py`

---

**Projet réalisé dans le cadre du cours LOG3000**
