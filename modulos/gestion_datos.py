# modulos/gestion_datos.py

from modulos.datos_basicos import pedir_texto, pedir_entero
from modulos.validaciones import normalizar
from modulos.funciones_utiles import imprimir_tabla, imprimir_titulo

inventario = []


def agregar_juguete():
    imprimir_titulo("AGREGAR JUGUETE")

    nombre = pedir_texto("Nombre: ")
    categoria = pedir_texto("Categoría (ej: muñecas, autos, peluches): ")

    nombre_norm = normalizar(nombre)

    # Validación de duplicado por nombre (usa normalizar en validaciones.py)
    for j in inventario:
        if normalizar(j["nombre"]) == nombre_norm:
            print(f"⚠️ Ya existe '{j['nombre']}' en el inventario (stock actual: {j['stock']}).")
            print("1. Sumar stock al existente")
            print("2. Cancelar y no agregar")

            opcion = pedir_entero("Elige opción (1-2): ", minimo=1, maximo=2)

            if opcion == 1:
                cantidad = pedir_entero("¿Cuánto stock quieres sumar?: ", minimo=1)
                j["stock"] += cantidad
                print(f"✅ Stock actualizado. Nuevo stock: {j['stock']}")
                return
            else:
                print("❌ Operación cancelada.")
                return

    precio = pedir_entero("Precio (solo número): ", minimo=1)
    stock = pedir_entero("Stock (0 o más): ", minimo=0)

    juguete = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }

    inventario.append(juguete)
    print("✅ Juguete agregado.")


def listar_juguetes():
    imprimir_titulo("INVENTARIO COMPLETO")

    if len(inventario) == 0:
        print("No hay juguetes cargados.")
        return

    imprimir_tabla(inventario)


def buscar_juguete_por_nombre():
    imprimir_titulo("BUSCAR JUGUETE")

    if len(inventario) == 0:
        print("No hay juguetes cargados.")
        return

    buscado = normalizar(pedir_texto("Nombre a buscar: "))

    resultados = []
    for j in inventario:
        if buscado in normalizar(j["nombre"]):
            resultados.append(j)

    if len(resultados) == 0:
        print("No se encontraron coincidencias.")
        return

    print(f"✅ Se encontraron {len(resultados)} resultado(s):")
    imprimir_tabla(resultados)


def eliminar_juguete():
    imprimir_titulo("ELIMINAR JUGUETE")

    if len(inventario) == 0:
        print("No hay juguetes cargados.")
        return

    imprimir_tabla(inventario)
    pos = pedir_entero("Número del juguete a eliminar: ", minimo=1, maximo=len(inventario))

    eliminado = inventario.pop(pos - 1)
    print(f"🗑️ Eliminado: {eliminado['nombre']}")


def actualizar_stock():
    imprimir_titulo("ACTUALIZAR STOCK")

    if len(inventario) == 0:
        print("No hay juguetes cargados.")
        return

    imprimir_tabla(inventario)
    pos = pedir_entero("Número del juguete a actualizar: ", minimo=1, maximo=len(inventario))

    juguete = inventario[pos - 1]
    print(f"Seleccionaste: {juguete['nombre']} (stock actual: {juguete['stock']})")

    print("1. Sumar stock")
    print("2. Restar stock")
    opcion = pedir_entero("Elige opción (1-2): ", minimo=1, maximo=2)

    cantidad = pedir_entero("Cantidad: ", minimo=1)

    if opcion == 1:
        juguete["stock"] += cantidad
        print(f"✅ Stock actualizado. Nuevo stock: {juguete['stock']}")
    else:
        if cantidad > juguete["stock"]:
            print("❌ No puedes restar más de lo que hay en stock.")
        else:
            juguete["stock"] -= cantidad
            print(f"✅ Stock actualizado. Nuevo stock: {juguete['stock']}")


def mostrar_stock_bajo(limite=3):
    imprimir_titulo(f"STOCK BAJO (<= {limite})")

    if len(inventario) == 0:
        print("No hay juguetes cargados.")
        return

    bajos = []
    for j in inventario:
        if j["stock"] <= limite:
            bajos.append(j)

    if len(bajos) == 0:
        print("✅ No hay juguetes con stock bajo.")
        return

    imprimir_tabla(bajos)


def resumen_inventario():
    imprimir_titulo("RESUMEN DEL INVENTARIO")

    if len(inventario) == 0:
        print("No hay juguetes cargados.")
        return

    productos_distintos = len(inventario)
    total_unidades = 0
    valor_total = 0
    categorias = set()

    for j in inventario:
        total_unidades += j["stock"]
        valor_total += j["stock"] * j["precio"]
        categorias.add(normalizar(j["categoria"]))

    print(f"Productos distintos: {productos_distintos}")
    print(f"Unidades totales (suma de stock): {total_unidades}")
    print(f"Categorías distintas: {len(categorias)}")
    print(f"Valor total del inventario: ${valor_total}")
