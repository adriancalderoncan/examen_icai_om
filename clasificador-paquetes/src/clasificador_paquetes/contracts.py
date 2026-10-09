from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator


class Entrada(BaseModel):
    # TODO
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    # id_paquete: texto. Elimina los espacios al principio y al final; después no puede estar vacío.
    id_paquete: str = Field(min_length=1, trim_whitespace=True)

    # peso_kg: número finito, mayor que 0 y menor o igual que 30.
    peso_kg: float = Field(gt=0, le=30)

    # distancia_km: número finito, entre 0 y 200, ambos incluidos.
    distancia_km: float = Field(ge=0, le=200)

class Salida(BaseModel):
    # TODO
    model_config = ConfigDict(extra="forbid")

    # id_paquete: texto no vacío.
    id_paquete: str = Field(min_length=1)

    # categoria: solo normal o urgente.
    categoria: Literal["normal", "urgente"]

    # confianza: número finito entre 0 y 1, ambos incluidos.
    confianza: float = Field(ge=0, le=1)
