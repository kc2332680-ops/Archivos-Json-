import json

# ==========================================
# 1. PREPARACIÓN DE DATOS (Archivos JSON)
# ==========================================
def crear_archivos_ejemplo():
    productos = [
        {"producto": "Monitor", "precio": 200, "cantidad": 10},
        {"producto": "Teclado", "precio": 30, "cantidad": 3},
        {"producto": "Mouse", "precio": 15, "cantidad": 2},
        {"producto": "Laptop", "precio": 800, "cantidad": 6}
    ]
    
    ventas = [
        {"vendedor": "Ana", "mes": "Enero", "ventas": 1200},
        {"vendedor": "Pedro", "mes": "Enero", "ventas": 900},
        {"vendedor": "Ana", "mes": "Febrero", "ventas": 1500},
        {"vendedor": "Pedro", "mes": "Febrero", "ventas": 1100},
        {"vendedor": "Luis", "mes": "Enero", "ventas": 2000}
    ]
    
    with open('productos.json', 'w') as f:
        json.dump(productos, f, indent=4)
    with open('ventas.json', 'w') as f:
        json.dump(ventas, f, indent=4)

# ==========================================
# 2. EJECUCIÓN DEL EJERCICIO 1: INVENTARIO
# ==========================================
def procesar_inventario():
    print("\n--- EJERCICIO 1: INVENTARIO ---")
    with open('productos.json', 'r') as f:
        productos = json.load(f)
    
    total_inventario = 0
    bajo_stock = []

    for p in productos:
        # Valor total por producto
        valor_total_producto = p['precio'] * p['cantidad']
        total_inventario += valor_total_producto
        
        print(f"Producto: {p['producto']} | Subtotal: ${valor_total_producto}")
        
        # Filtro bajo stock (< 5)
        if p['cantidad'] < 5:
            bajo_stock.append(p)

    print(f"VALOR TOTAL DEL INVENTARIO: ${total_inventario}")
    
    # Exportar bajo stock
    with open('bajo_stock.json', 'w') as f:
        json.dump(bajo_stock, f, indent=4)
    print("-> Archivo 'bajo_stock.json' creado.")

# ==========================================
# 3. EJECUCIÓN DEL EJERCICIO 2: VENTAS
# ==========================================
def procesar_ventas():
    print("\n--- EJERCICIO 2: VENTAS ---")
    with open('ventas.json', 'r') as f:
        ventas_data = json.load(f)

    # Diccionario para acumular ventas por nombre
    agrupado = {}
    total_acumulado_ventas = 0

    for v in ventas_data:
        nombre = v['vendedor']
        monto = v['ventas']
        total_acumulado_ventas += monto
        
        if nombre not in agrupado:
            agrupado[nombre] = []
        agrupado[nombre].append(monto)

    # Crear ranking
    ranking = []
    for nombre, lista_ventas in agrupado.items():
        total_v = sum(lista_ventas)
        promedio_v = total_v / len(lista_ventas)
        ranking.append({
            "vendedor": nombre,
            "total_ventas": total_v,
            "promedio_mensual": promedio_v
        })

    # Promedio mensual general (de todos los registros)
    promedio_general = total_acumulado_ventas / len(ventas_data)
    print(f"Promedio mensual de todas las ventas: ${promedio_general:.2f}")

    # Vendedor con mayores ventas (Ordenar ranking)
    ranking_ordenado = sorted(ranking, key=lambda x: x['total_ventas'], reverse=True)
    top_vendedor = ranking_ordenado[0]
    
    print(f"Vendedor con más ventas: {top_vendedor['vendedor']} (${top_vendedor['total_ventas']})")

    # Exportar ranking
    with open('ranking_ventas.json', 'w') as f:
        json.dump(ranking_ordenado, f, indent=4)
    print("-> Archivo 'ranking_ventas.json' creado.")

# ==========================================
# BLOQUE PRINCIPAL
# ==========================================
if __name__ == "__main__":
    crear_archivos_ejemplo()  # Genera los archivos necesarios
    procesar_inventario()     # Resuelve el ejercicio 1
    procesar_ventas()         # Resuelve el ejercicio 2