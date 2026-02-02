# modulos/validaciones.py
# Lección 3: validaciones con condicionales

def normalizar(texto):
    return texto.strip().lower()


def validar_no_vacio(valor):
    """
    Retorna True si el texto NO está vacío.
    """
    if valor == "":
        return False
    return True


def validar_entero(valor, minimo=None, maximo=None):
    """
    Retorna True si:
    - valor es dígito
    - y cumple rango opcional [minimo, maximo]
    """
    if not valor.isdigit():
        return False

    numero = int(valor)

    if minimo is not None and numero < minimo:
        return False
    elif maximo is not None and numero > maximo:
        return False

    return True


def validar_opcion(valor, minimo, maximo):
    """
    Valida que la opción sea un entero dentro de un rango.
    """
    if not validar_entero(valor, minimo, maximo):
        return False
    return True
