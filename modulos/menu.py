# modulos/menu.py

from modulos.gestion_datos import (
    agregar_juguete,
    listar_juguetes,
    buscar_juguete_por_nombre,
    eliminar_juguete,
    actualizar_stock,
    mostrar_stock_bajo,
    resumen_inventario
)

from modulos.funciones_utiles import pausar, imprimir_titulo
from modulos.datos_basicos import pedir_entero


def mostrar_menu():
    while True:
        imprimir_titulo("TIENDA DE JUGUETES - SISTEMA DE INVENTARIO")
        print("1. Agregar juguete")
        print("2. Mostrar inventario completo")
        print("3. Buscar juguete por nombre")
        print("4. Eliminar juguete")
        print("5. Actualizar stock")
        print("6. Ver juguetes con stock bajo")
        print("7. Ver resumen del inventario")
        print("0. Salir")

        opcion = pedir_entero("Selecciona una opción: ", minimo=0, maximo=7)

        if opcion == 1:
            agregar_juguete()
            pausar()
        elif opcion == 2:
            listar_juguetes()
            pausar()
        elif opcion == 3:
            buscar_juguete_por_nombre()
            pausar()
        elif opcion == 4:
            eliminar_juguete()
            pausar()
        elif opcion == 5:
            actualizar_stock()
            pausar()
        elif opcion == 6:
            mostrar_stock_bajo()
            pausar()
        elif opcion == 7:
            resumen_inventario()
            pausar()
        elif opcion == 0:
            print("👋 Saliendo del sistema...")
            break
