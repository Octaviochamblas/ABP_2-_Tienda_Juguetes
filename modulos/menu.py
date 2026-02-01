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

def mostrar_menu():
    while True:
        print("\n=== TIENDA DE JUGUETES - SISTEMA DE INVENTARIO ===")
        print("1. Agregar juguete")
        print("2. Mostrar inventario completo")
        print("3. Buscar juguete por nombre")
        print("4. Eliminar juguete")
        print("5. Actualizar stock")
        print("6. Ver juguetes con stock bajo")
        print("7. Ver resumen del inventario")
        print("0. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            agregar_juguete()
        elif opcion == "2":
            listar_juguetes()
        elif opcion == "3":
            buscar_juguete_por_nombre()
        elif opcion == "4":
            eliminar_juguete()
        elif opcion == "5":
            actualizar_stock()
        elif opcion == "6":
            mostrar_stock_bajo()
        elif opcion == "7":
            resumen_inventario()
        elif opcion == "0":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")
