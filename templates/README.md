# Module `templates/`

## Raison d'être

Le répertoire `templates/` contient tous les fichiers de templates HTML utilisés par Flask pour générer les pages web dynamiques. Flask utilise le moteur de templates Jinja2 pour rendre ces fichiers, permettant l'injection de variables Python, l'utilisation de structures de contrôle, et l'héritage de templates.

Dans cette application, les templates définissent l'interface utilisateur de la calculatrice et permettent la communication bidirectionnelle entre le client (navigateur) et le serveur (Flask).

## Fichiers et responsabilités

### `index.html`

**Responsabilité principale :** Template principal de l'application, définissant l'interface utilisateur complète de la calculatrice.

**Structure et sections :**

1. **En-tête HTML (`<head>`)**
   - Définit les métadonnées (charset, viewport)
   - Lie le fichier CSS via `url_for('static', filename='style.css')`
   - Définit le titre de la page

2. **Formulaire principal (`<form>`)**
   - Méthode POST pour envoyer les expressions à calculer au serveur
   - Champ d'affichage (`#display`) : Affiche le résultat ou l'expression en cours
     - Rempli dynamiquement via la variable Jinja2 `{{ result }}`
     - En lecture seule pour éviter la saisie manuelle

3. **Grille de boutons (`<div class="buttons">`)**
   - **Boutons numériques** : Chiffres 0-9 pour construire les opérandes
   - **Boutons opérateurs** : +, -, *, / pour les opérations arithmétiques
   - **Bouton Clear (C)** : Efface le champ d'affichage
   - **Bouton Égal (=)** : Soumet le formulaire pour calculer

4. **Scripts JavaScript**
   - `appendToDisplay(value)` : Ajoute un caractère au champ d'affichage
   - `clearDisplay()` : Vide complètement le champ d'affichage
   - Gère l'interactivité côté client avant la soumission au serveur

**Flux de données :**
1. L'utilisateur clique sur les boutons → JavaScript ajoute les caractères au display
2. L'utilisateur clique sur "=" → Le formulaire est soumis en POST
3. Flask traite la requête → Calcule le résultat via `calculate()`
4. Flask rend le template avec `{{ result }}` → Le résultat s'affiche dans le display

## Dépendances et hypothèses

### Dépendances
- **Flask** : Le framework Flask doit être configuré pour utiliser Jinja2 (configuration par défaut)
- **Fichier CSS** : `static/style.css` doit exister et être accessible
- **Route Flask** : La route `/` dans `app.py` doit rendre ce template avec la variable `result`

### Hypothèses
- **Variables Jinja2 attendues** :
  - `result` : Le résultat du calcul ou une chaîne vide (string)
- **Structure backend** :
  - La route `/` accepte les méthodes GET et POST
  - Le formulaire envoie les données via le champ `name="display"`
  - Les erreurs sont capturées et affichées dans le format `"Error: <message>"`
- **Navigateur moderne** : Supporte JavaScript et les fonctionnalités HTML5 utilisées

## Intégration avec Flask

### Utilisation dans `app.py`

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)
```

### Variables passées au template

- `result` : Le résultat du calcul (float converti en string) ou un message d'erreur
  - En GET : chaîne vide
  - En POST (succès) : résultat numérique
  - En POST (erreur) : `"Error: <message d'erreur>"`

## Pour les nouveaux développeurs

### Comment modifier l'interface

1. **Modifier les boutons** :
   - Ajoutez/supprimez des boutons dans la section `<div class="buttons">`
   - Respectez la structure de grille 4 colonnes définie dans CSS
   - Utilisez `onclick="appendToDisplay('...')"` pour les boutons de saisie

2. **Ajouter de nouvelles fonctionnalités JavaScript** :
   - Ajoutez vos fonctions dans la section `<script>`
   - Utilisez `document.getElementById('display')` pour accéder au champ d'affichage

3. **Modifier le formulaire** :
   - Le formulaire doit rester en méthode POST pour envoyer les données au serveur
   - Le champ `name="display"` est requis pour que Flask récupère l'expression

### Ajout de nouveaux templates

Si vous devez créer de nouvelles pages :

1. Créez un nouveau fichier `.html` dans ce répertoire
2. Utilisez la fonction `render_template('nouveau_template.html', ...)` dans `app.py`
3. Suivez la même structure que `index.html` pour la cohérence visuelle

### Syntaxe Jinja2 utilisée

- `{{ result }}` : Affiche la variable `result` (échappée automatiquement)
- `{{ url_for('static', filename='style.css') }}` : Génère l'URL vers un fichier statique
- Pour des structures plus complexes (boucles, conditions), consultez la [documentation Jinja2](https://jinja.palletsprojects.com/)

### Points d'attention

- **Sécurité** : Jinja2 échappe automatiquement les variables pour prévenir XSS
- **Interactivité** : Les boutons utilisent `type="button"` sauf le bouton "=" qui est `type="submit"`
- **Accessibilité** : Le champ d'affichage est en `readonly` pour éviter la saisie manuelle et garantir la cohérence avec l'interface boutons

