"""
Application Flask pour une calculatrice web simple.

Ce module implémente une calculatrice qui accepte des expressions arithmétiques
de la forme "nombre opérateur nombre" et affiche le résultat.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Dictionnaire associant les symboles d'opérateurs à leurs fonctions correspondantes
# Permet une recherche et exécution dynamique des opérations
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Évalue une expression arithmétique simple de la forme "nombre opérateur nombre".
    
    Parse l'expression, valide le format, extrait les opérandes et l'opérateur,
    puis effectue le calcul correspondant.
    
    Args:
        expr (str): Expression arithmétique à évaluer (ex: "5 + 3", "10 * 2")
    
    Returns:
        float: Le résultat du calcul
    
    Raises:
        ValueError: Si l'expression est vide, invalide, contient plusieurs opérateurs,
                   ou si les opérandes ne sont pas des nombres valides
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Supprime les espaces pour simplifier le parsing
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Recherche de l'opérateur dans l'expression
    # Parcourt chaque caractère pour trouver le premier opérateur valide
    for i, ch in enumerate(s):
        if ch in OPS:
            # Vérifie qu'un seul opérateur est présent (contrainte de la calculatrice simple)
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Vérifie que l'opérateur est au milieu de l'expression avec des opérandes de chaque côté
    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    # Sépare l'expression en opérande gauche et droit
    left = s[:op_pos]
    right = s[op_pos+1:]

    # Conversion des opérandes en nombres flottants
    # Utilise float() plutôt que int() pour supporter les nombres décimaux
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Exécute l'opération correspondante via le dictionnaire OPS
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application.
    
    Gère l'affichage initial de la calculatrice (GET) et le traitement
    des calculs soumis via le formulaire (POST).
    
    Returns:
        str: Le template HTML rendu avec le résultat du calcul (ou chaîne vide)
    """
    result = ""
    # Traite uniquement les requêtes POST (soumission du formulaire)
    if request.method == 'POST':
        # Récupère l'expression depuis le champ 'display' du formulaire
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # Affiche l'erreur à l'utilisateur plutôt que de planter l'application
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Point d'entrée pour l'exécution directe du script
    # Démarre le serveur Flask en mode développement
    app.run(debug=True)