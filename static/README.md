# Module `static/`

## Raison d'être

Le répertoire `static/` contient tous les fichiers statiques (assets) de l'application Flask qui sont servis directement au client sans traitement par le serveur. Ces fichiers incluent les styles CSS, les images, les scripts JavaScript externes, et autres ressources statiques nécessaires au rendu de l'interface utilisateur.

Dans Flask, les fichiers dans le répertoire `static/` sont accessibles via l'URL `/static/...`, ce qui permet une séparation claire entre le code serveur et les ressources client.

## Fichiers et responsabilités

### `style.css`

**Responsabilité principale :** Définit tous les styles visuels de l'application calculatrice.

**Contenu :**
- **Layout général** : Styles pour le body, centrage de la calculatrice sur la page
- **Conteneur calculatrice** : Styles pour la boîte principale (fond sombre, ombres, bordures arrondies)
- **Champ d'affichage** : Styles pour l'écran de la calculatrice (input en lecture seule)
- **Grille de boutons** : Organisation en grille CSS Grid (4 colonnes)
- **Styles de boutons** : Styles de base pour tous les boutons (numériques et opérateurs)
- **Styles d'opérateurs** : Distinction visuelle des opérateurs (couleur orange)
- **Effets interactifs** : États hover et active pour le feedback visuel

**Approche de design :**
- Thème sombre avec contraste élevé pour la lisibilité
- Utilisation de CSS Grid pour une disposition responsive
- Transitions CSS pour les effets de survol et de clic
- Design moderne et épuré inspiré des calculatrices iOS

## Dépendances et hypothèses

### Dépendances
- **Flask** : Le framework Flask doit être configuré pour servir les fichiers statiques (configuration par défaut)
- **Navigateur moderne** : Utilise CSS Grid et les propriétés CSS3 modernes
- **Templates HTML** : Les templates doivent référencer les fichiers CSS via `url_for('static', filename='style.css')`

### Hypothèses
- Les templates utilisent les classes CSS définies dans `style.css` :
  - `.calculator` : conteneur principal
  - `.btn` : boutons numériques
  - `.operator` : boutons d'opérateurs
  - `#display` : champ d'affichage
  - `.buttons` : conteneur de la grille de boutons
- Le navigateur supporte les propriétés CSS modernes (Grid, transitions, etc.)
- Les polices système Arial sont disponibles (fallback vers sans-serif)

## Structure attendue

Pour que les styles fonctionnent correctement, le template HTML doit respecter la structure suivante :

```html
<div class="calculator">
  <h1>Titre</h1>
  <form>
    <input type="text" id="display" ...>
    <div class="buttons">
      <button class="btn">...</button>
      <button class="btn operator">...</button>
    </div>
  </form>
</div>
```

## Pour les nouveaux développeurs

### Comment modifier les styles

1. **Modifier les couleurs** : Cherchez les valeurs hexadécimales (`#333`, `#ff9500`, etc.) dans `style.css`
2. **Modifier la disposition** : La grille de boutons utilise `grid-template-columns: repeat(4, 1fr)` pour 4 colonnes
3. **Ajouter de nouveaux styles** : Créez de nouvelles classes ou modifiez les existantes en respectant la convention de nommage

### Points d'attention

- Les styles utilisent des unités relatives (`rem`, `%`, `fr`) pour la responsivité
- Les transitions CSS sont définies pour améliorer l'expérience utilisateur
- Les couleurs des opérateurs sont distinctes pour améliorer la distinction visuelle

### Ajout de nouveaux fichiers statiques

Si vous devez ajouter d'autres fichiers statiques (images, scripts JavaScript externes, etc.) :
1. Placez-les dans ce répertoire `static/`
2. Référencez-les dans les templates via `url_for('static', filename='nom_du_fichier')`
3. Créez des sous-répertoires si nécessaire (ex: `static/images/`, `static/js/`)

