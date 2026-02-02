# modulos/datos_basicos.py
# Lección 2: carga de datos básicos

from modulos.validaciones import validar_no_vacio, validar_entero


def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if validar_no_vacio(valor):
            return valor
        print("❌ No puede estar vacío.")


def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        valor = input(mensaje).strip()
        if validar_entero(valor, minimo, maximo):
            return int(valor)
        print("❌ Número inválido.")
