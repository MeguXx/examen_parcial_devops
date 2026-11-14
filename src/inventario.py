import csv
import requests

def obtener_datos(url="https://dummyjson.com/products"):
    """Obtiene los datos desde la API REST sobre HTTPS."""
    try:
        respuesta = requests.get(url, timeout=10)
        if respuesta.status_code == 200:
            print("Conexion exitosa a la API (Codigo HTTP 200 OK)")
            return respuesta.json()
        else:
            print("Error al conectar con la API")
            print("Codigo de estado:", respuesta.status_code)
            return None
    except requests.exceptions.RequestException as error:
        print("Error de red o conexion HTTPS:", error)
        return None

def generar_csv(datos):
    """Procesa los datos JSON y genera el archivo CSV del inventario."""
    if not datos or "products" not in datos:
        print("No se encontraron datos validos para generar el CSV")
        return

    with open("data/inventario.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["ID", "PRODUCTO", "PRECIO"])
        for producto in datos["products"]:
            escritor.writerow([
                producto["id"],
                producto["title"],
                producto["price"],
            ])
    print("Archivo data/inventario.csv generado correctamente")

def main():
    datos = obtener_datos()
    if datos:
        generar_csv(datos)

if __name__ == "__main__":
    main()
