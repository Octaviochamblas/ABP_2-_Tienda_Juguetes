# modulos/funciones_utiles.py
# Lección 6: funciones generales reutilizables

def pausar():
    input("\nPresiona Enter para continuar...")


def imprimir_titulo(texto):
    print("\n" + "=" * 55)
    print(texto)
    print("=" * 55)


def imprimir_tabla(lista):
    """
    Imprime una lista de juguetes en formato tabla.
    Espera diccionarios con: nombre, categoria, precio, stock
    """
    if len(lista) == 0:
        print("No hay registros para mostrar.")
        return

    print("\nN°  | Nombre                      | Categoría           | Precio    | Stock")
    print("-" * 75)

    for i, j in enumerate(lista, start=1):
        nombre = j["nombre"][:26]
        categoria = j["categoria"][:18]
        precio = j["precio"]
        stock = j["stock"]
        print(f"{i:<3} | {nombre:<26} | {categoria:<18} | ${precio:<7} | {stock}")
