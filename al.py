from sympy.parsing.sympy_parser import parse_expr
from flask import Flask, request, jsonify
from sympy.logic.boolalg import Or, And, Not
from sympy import symbols, simplify_logic
import re

app = Flask(__name__)

def simplificar(expresion, form='dnf'):
    """
    Esta función simplifica la expresión lógica usando simplify_logic de SymPy y la fuerza a la forma dada.
    """
    return simplify_logic(expresion, form=form)

def convertir_a_sympy(expresion_str, variables):
    """
    Convierte la cadena de texto con la expresión lógica en una expresión simbólica de SymPy.
    """
    # Reemplazar los símbolos lógicos estándar por los símbolos que SymPy entiende
    simbolos = {
        "∧": "&",   # AND
        "∨": "|",   # OR
        "¬": "~",   # NOT
        "→": ">>",  # Implica
        "↔": "==",  # Equivalente
        "⊕": "^"    # XOR (Disyunción Excluyente)
    }
    for simbolo, reemplazo in simbolos.items():
        expresion_str = expresion_str.replace(simbolo, reemplazo)

    # Definir el contexto para parse_expr dinámicamente con las variables
    contexto = {var: variables[var] for var in variables}

    try:
        # Convertir la cadena a una expresión simbólica de SymPy
        return parse_expr(expresion_str, local_dict=contexto)
    except Exception as e:
        print(f"Error al convertir la expresión: {e}")
        return None

def revertir_simbolos(expresion_str):
    """
    Convierte los operadores de SymPy a los símbolos originales ingresados por el usuario.
    """
    simbolos_revertidos = {
        "&": "∧",   # AND
        "|": "∨",   # OR
        "~": "¬",   # NOT
        ">>": "→",  # Implica
        "==": "↔",  # Equivalente
        "^": "⊕"    # XOR (Disyunción Excluyente)
    }
    for simbolo, reemplazo in simbolos_revertidos.items():
        expresion_str = expresion_str.replace(simbolo, reemplazo)
    return expresion_str

def extraer_variables(expresion_str):
    """
    Extrae las variables de la expresión lógica en formato de texto.
    """
    return sorted(set(re.findall(r'[A-Za-z]+', expresion_str)))

@app.route('/simplificar', methods=['POST'])
def simplificar_expresion():
    # Obtener la expresión lógica desde el cuerpo de la solicitud
    data = request.get_json()
    if not data or 'expresion' not in data:
        return jsonify({"error": "Debe proporcionar una expresión lógica"}), 400
    
    expresion_str = data['expresion']
    
    # Extraer las variables de la expresión
    nombres_variables = extraer_variables(expresion_str)
    variables = {nombre: symbols(nombre) for nombre in nombres_variables}

    # Convertir la cadena de texto a una expresión simbólica
    try:
        expresion = convertir_a_sympy(expresion_str, variables)
        if not expresion:
            return jsonify({"error": "Error al convertir la expresión lógica"}), 400

        # Simplificar la expresión
        expresion_simplificada = simplificar(expresion, form='dnf')

        # Convertir las expresiones de vuelta a los símbolos originales
        expresion_simplificada_revertida = revertir_simbolos(str(expresion_simplificada))

        return jsonify({
            'expresion_original': str(expresion_str),
            'expresion_simplificada': str(expresion_simplificada_revertida)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
