from sympy import symbols, Or, And, Not, simplify_logic
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

# Definir las variables lógicas
A, B, C = symbols('A B C')

def convertir_a_sympy(expresion):
    """
    Convierte la cadena de texto con la expresión lógica en una expresión simbólica de SymPy.
    """
    # Reemplazar los operadores lógicos por los equivalentes en SymPy
    expresion = expresion.replace("and", "&").replace("or", "|").replace("not", "~")
    
    # Intentamos convertir la cadena a una expresión de SymPy
    try:
        return parse_expr(expresion, transformations=standard_transformations + (implicit_multiplication_application,))
    except Exception as e:
        print(f"Error al convertir la expresión: {e}")
        return None

def ley_absorcion(expresion):
    """
    Verifica si la ley de absorción A | (A & B) = A se aplica.
    """
    if isinstance(expresion, Or) and len(expresion.args) == 2:
        # Verifica si la forma es A | (A & B)
        if isinstance(expresion.args[1], And) and expresion.args[0] == expresion.args[1].args[0]:
            return True
    return False

def ley_idempotencia(expresion):
    """
    Verifica si la ley de idempotencia A | A = A o A & A = A se aplica.
    """
    if isinstance(expresion, Or) and len(expresion.args) == 2 and expresion.args[0] == expresion.args[1]:
        return True
    if isinstance(expresion, And) and len(expresion.args) == 2 and expresion.args[0] == expresion.args[1]:
        return True
    return False

def ley_exclusion(expresion):
    """
    Verifica si la ley de exclusión A | ~A = True o A & ~A = False se aplica.
    """
    if isinstance(expresion, Or):
        for arg in expresion.args:
            if isinstance(arg, Not) and arg.args[0] == expresion.args[0]:
                return True
    if isinstance(expresion, And):
        for arg in expresion.args:
            if isinstance(arg, Not) and arg.args[0] == expresion.args[0]:
                return True
    return False

def detectar_leyes(expresion):
    """
    Detecta las leyes lógicas que pueden aplicarse a la expresión lógica de manera recursiva.
    """
    leyes_detectadas = []

    # Verificar las leyes en la expresión actual
    if ley_absorcion(expresion):
        leyes_detectadas.append("Ley de absorción: A | (A & B) = A")
    
    if ley_idempotencia(expresion):
        leyes_detectadas.append("Ley de idempotencia: A | A = A o A & A = A")
    
    if ley_exclusion(expresion):
        leyes_detectadas.append("Ley de exclusión: A | ~A = True o A & ~A = False")
    
    # Recorrer recursivamente los argumentos (sub-expresiones)
    if hasattr(expresion, 'args'):
        for subexpresion in expresion.args:
            leyes_detectadas.extend(detectar_leyes(subexpresion))

    return leyes_detectadas

# Entrada del usuario
entrada_usuario = input("Introduce una expresión lógica utilizando A, B, C y los operadores 'not', 'and', 'or' (por ejemplo: (A and B) or (A and not B)): ")

# Convertir la cadena de texto a una expresión simbólica
expresion = convertir_a_sympy(entrada_usuario)

# Si la expresión es válida, simplificamos y detectamos las leyes
if expresion:
    # Detectar las leyes que se pueden aplicar
    leyes_aplicadas = detectar_leyes(expresion)

    # Mostrar los resultados
    if leyes_aplicadas:
        print("Leyes detectadas que pueden aplicarse:")
        for ley in leyes_aplicadas:
            print(f"- {ley}")
    else:
        print("No se detectaron leyes que puedan aplicarse.")
