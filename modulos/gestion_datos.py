# modulos/gestion_datos.py

# "Base de datos" en memoria: lista de diccionarios
inventario = []

# modulos/gestion_datos.py

inventario = []

def agregar_juguete():
    print("\n--- AGREGAR JUGUETE ---")
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría (ej: muñecas, autos, peluches): ").strip()

    # Normalizamos nombre para comparar
    nombre_normalizado = nombre.lower()

    # Verificar duplicado por nombre
    for j in inventario:
        if j["nombre"].strip().lower() == nombre_normalizado:
            print(f"⚠️ Ya existe '{j['nombre']}' en el inventario (stock actual: {j['stock']}).")
            print("1. Sumar stock al existente")
            print("2. Cancelar y no agregar")
            opcion = input("Elige opción: ").strip()

            if opcion == "1":
                while True:
                    stock_txt = input("¿Cuánto stock quieres sumar?: ").strip()
                    if stock_txt.isdigit() and int(stock_txt) > 0:
                        j["stock"] += int(stock_txt)
                        print(f"✅ Stock actualizado. Nuevo stock: {j['stock']}")
                        return
                    print("❌ Cantidad inválida.")
            else:
                print("❌ Operación cancelada.")
                return

    # Si NO es duplicado, pedimos precio y stock normalmente
    while True:
        precio_txt = input("Precio (solo número): ").strip()
        if precio_txt.isdigit() and int(precio_txt) > 0:
            precio = int(precio_txt)
            break
        print("❌ Precio inválido. Intenta de nuevo.")

    while True:
        stock_txt = input("Stock (0 o más): ").strip()
        if stock_txt.isdigit():
            stock = int(stock_txt)
            break
        print("❌ Stock inválido. Intenta de nuevo.")

    juguete = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }

    inventario.append(juguete)
    print("✅ Juguete agregado.")

def listar_juguetes():
    print("\n--- INVENTARIO COMPLETO ---")
    if len(inventario) == 0:
        print("No hay juguetes cargados.")
        return

    _imprimir_tabla(inventario)


def buscar_juguete_por_nombre():
    print("\n--- BUSCAR JUGUETE ---")
    if len(inventario) == 0:
        print("No hay juguetes cargados.")
        return

    buscado = input("Nombre a buscar: ").strip().lower()

    resultados = []
    for j in inventario:
        if buscado in j["nombre"].lower():
            resultados.append(j)

    if len(resultados) == 0:
        print("No se encontraron coincidencias.")
        return

    print(f"✅ Se encontraron {len(resultados)} resultado(s):")
    _imprimir_tabla(resultados)


def eliminar_juguete():
    print("\n--- ELIMINAR JUGUETE ---")
    if len(inventario) == 0:
        print("No hay juguetes cargados.")
        return

    listar_juguetes()

    while True:
        pos_txt = input("Ingresa el número del juguete a eliminar: ").strip()
        if pos_txt.isdigit():
            pos = int(pos_txt)
            if 1 <= pos <= len(inventario):
                eliminado = inventario.pop(pos - 1)
                print(f"🗑️ Eliminado: {eliminado['nombre']}")
                return
        print("❌ Número inválido. Intenta otra vez.")
def actualizar_stock():
    print("\n--- ACTUALIZAR STOCK ---")
    if len(inventario) == 0:
        print("No hay juguetes cargados.")
        return

    listar_juguetes()

    while True:
        pos_txt = input("Número del juguete a actualizar: ").strip()
        if pos_txt.isdigit():
            pos = int(pos_txt)
            if 1 <= pos <= len(inventario):
                break
        print("❌ Número inválido. Intenta otra vez.")

    juguete = inventario[pos - 1]
    print(f"Seleccionaste: {juguete['nombre']} (stock actual: {juguete['stock']})")

    print("1. Sumar stock")
    print("2. Restar stock")

    opcion = input("Elige opción: ").strip()

    while True:
        cant_txt = input("Cantidad: ").strip()
        if cant_txt.isdigit() and int(cant_txt) > 0:
            cantidad = int(cant_txt)
            break
        print("❌ Cantidad inválida.")

    if opcion == "1":
        juguete["stock"] += cantidad
        print(f"✅ Stock actualizado. Nuevo stock: {juguete['stock']}")
    elif opcion == "2":
        if cantidad > juguete["stock"]:
            print("❌ No puedes restar más de lo que hay en stock.")
        else:
            juguete["stock"] -= cantidad
            print(f"✅ Stock actualizado. Nuevo stock: {juguete['stock']}")
    else:
        print("❌ Opción inválida.")
        
def mostrar_stock_bajo(limite=3):
    print(f"\n--- JUGUETES CON STOCK BAJO (<= {limite}) ---")

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

    _imprimir_tabla(bajos)


def resumen_inventario():
    print("\n--- RESUMEN DEL INVENTARIO ---")

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
        categorias.add(j["categoria"].strip().lower())

    print(f"Productos distintos: {productos_distintos}")
    print(f"Unidades totales (suma de stock): {total_unidades}")
    print(f"Categorías distintas: {len(categorias)}")
    print(f"Valor total del inventario: ${valor_total}")

def _imprimir_tabla(lista):
    """Imprime una lista de juguetes en formato de tabla."""
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


