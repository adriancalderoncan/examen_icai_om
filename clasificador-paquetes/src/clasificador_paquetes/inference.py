import csv
from pathlib import Path
import joblib
from .contracts import Entrada, Salida


def leer_csv(ruta: Path) -> list[Entrada]:
    # TODO

    with open(ruta, mode="r", newline="", encoding="utf8") as f:
        dataset = csv.DictReader(f)
        lista_entradas = []
        for row in dataset:
                entrada = Entrada(**row)
                lista_entradas.append(entrada)

    if not lista_entradas:
        raise ValueError("El CSV no contiene filas")

    return lista_entradas


def preprocesar(entrada: Entrada) -> list[float]:
    # TODO

    peso_redondeado = round(entrada.peso_kg, 1)
    distancia = entrada.distancia_km
    return [peso_redondeado, distancia]


def cargar_modelo(ruta: Path):
    # TODO

    modelo = joblib.load(ruta)

    return modelo

def predecir(entrada: Entrada, modelo) -> Salida:
    # TODO
    #salidaç pizarra["normal", "urgente"]

    vector = preprocesar(entrada)
    # a 2d
    matriz = [vector] 
    categoria_predicha = modelo.predict(matriz)[0]
    probabilidades = modelo.predict_proba(matriz)[0]
    confianza = max(probabilidades) 

    salida = Salida(id_paquete=entrada.id_paquete, categoria=categoria_predicha, confianza=confianza)
    return salida


def guardar_csv(resultados: list[Salida], ruta: Path) -> None:
    # TODO

    with open(ruta, mode="w", newline="", encoding="utf8") as f:
        cabecera = ["id_paquete", "categoria", "confianza"]
        escribir = csv.DictWriter(f, fieldnames=cabecera)
        escribir.writeheader()
        for resultado in resultados:
            escribir.writerow(resultado.dict())


def ejecutar(entrada: Path, modelo: Path, salida: Path) -> None:
    # TODO

    entradas = leer_csv(entrada)
    modelo_cargado = cargar_modelo(modelo)
    resultados = []
    for entrada in entradas:
        resultado = predecir(entrada, modelo_cargado)
        resultados.append(resultado)

    guardar_csv(resultados, salida)


if __name__ == "__main__":
    ejecutar(
        Path("data/raw/paquetes.csv"),
        Path("models/modelo.joblib"),
        Path("resultados.csv"),
    )
