import pandas as pd

# Enlace del archivo JSON
enlace = "https://raw.githubusercontent.com/CesarMCuellarCha/archivosCSV/refs/heads/main/SENA.matriculados.json"

try:
    # -------------------------
    # 1. CARGAR INFORMACIÓN
    # -------------------------
    datos = pd.read_json(enlace)

    print("=== SISTEMA SENA INICIADO ===")
    print("\nCampos disponibles en el archivo:")
    print(datos.columns)

    # -------------------------
    # 2. INGRESAR NUEVO APRENDIZ
    # -------------------------
    print("\n=== Registro de Nuevo Aprendiz ===")

    nombre_aprendiz = input("Ingrese el nombre del aprendiz: ")
    ficha_aprendiz = input("Ingrese el número de ficha: ")

    registro_nuevo = {
        "NOMBRE": nombre_aprendiz,
        "FICHA": ficha_aprendiz,
        "PROGRAMA_FORMACION": "ANALISIS Y DESARROLLO DE SOFTWARE",
        "CODIGO_PROGRAMA": 228118,
        "ESTADO_APRENDIZ": "En transito"
    }

    # Añadir registro al DataFrame
    datos = pd.concat([datos, pd.DataFrame([registro_nuevo])], ignore_index=True)

    print("Aprendiz registrado correctamente.")

    # -------------------------
    # 3. FILTRAR PROGRAMA ADSO
    # -------------------------
    programa_adso = datos[datos["PROGRAMA_FORMACION"] == "ANALISIS Y DESARROLLO DE SOFTWARE"]

    # -------------------------
    # 4. BUSCAR FICHA ESPECÍFICA
    # -------------------------
    ficha_3312932 = programa_adso[programa_adso["FICHA"].astype(str) == "3312932"]

    # -------------------------
    # 5. FILTRAR POR CÓDIGO Y ESTADO
    # -------------------------
    aprendices_transito = datos[
        (datos["CODIGO_PROGRAMA"].astype(str) == "228118") &
        (datos["ESTADO_APRENDIZ"].str.contains("En transito", case=False, na=False))
    ]

    # -------------------------
    # 6. MOSTRAR ESTADÍSTICAS
    # -------------------------
    print("\n=== REPORTE GENERAL ===")

    print(f"Cantidad de aprendices en ADSO: {len(programa_adso)}")
    print(f"Cantidad en la ficha 3312932: {len(ficha_3312932)}")
    print(f"Aprendices en estado 'En transito' (228118): {len(aprendices_transito)}")

    # -------------------------
    # 7. GUARDAR RESULTADOS
    # -------------------------
    programa_adso.to_json("Listado_ADSO.json", orient="records", indent=4)

    aprendices_transito.to_csv("Aprendices_En_Transito.csv", index=False)

    print("\nArchivos generados con éxito:")
    print(" Listado_ADSO.json")
    print(" Aprendices_En_Transito.csv")

except Exception as error:
    print(f"Ocurrió un error en la ejecución: {error}")