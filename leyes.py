from sympy.logic.boolalg import Or, And, Not, Xor, Implies, Equivalent
from sympy import symbols, simplify_logic
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr

# Definir las variables lógicas
A, B, C = symbols('A B C')

def simplificar(expresion, form='dnf'):
    """
    Esta función simplifica la expresión lógica usando simplify_logic de SymPy y la fuerza a la forma dada.
    """
    return simplify_logic(expresion, form=form)

def convertir_a_sympy(expresion_str):
    """
    Convierte la cadena de texto con la expresión lógica en una expresión simbólica de SymPy.
    """
    # Definir el contexto para parse_expr
    contexto = {
        'And': And,
        'Or': Or,
        'Not': Not,
        'Xor': Xor,
        'Implies': Implies,
        'Equivalent': Equivalent,
        'A': A,
        'B': B,
        'C': C
    }

    # Transformaciones estándar
    transformations = standard_transformations + (implicit_multiplication_application,)

    # Intentar convertir la cadena a una expresión lógica con SymPy
    try:
        return parse_expr(expresion_str, local_dict=contexto, transformations=transformations)
    except Exception as e:
        print(f"Error al convertir la expresión: {e}")
        return None

# Obtener la expresión lógica del usuario
entrada_usuario = input("Introduce una expresión lógica utilizando A, B, C y los operadores 'Not', 'And', 'Or', 'Xor', 'Implies', 'Equivalent': ")

# Convertir la cadena de texto a una expresión simbólica
expresion = convertir_a_sympy(entrada_usuario)

if expresion:
    # Simplificación forzada a la forma normal disyuntiva (DNF)
    expresion_simplificada = simplificar(expresion, form='dnf')

    # Mostrar resultados
    print(f"Expresión original: {expresion}")
    print(f"Expresión simplificada: {expresion_simplificada}")
