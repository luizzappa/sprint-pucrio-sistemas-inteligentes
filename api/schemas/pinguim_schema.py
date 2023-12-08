from enum import Enum
from pydantic import BaseModel


class IslandEnum(int, Enum):
    Dream = 0
    Biscoe = 1
    Torgersen = 2


class SexEnum(int, Enum):
    Female = 0
    Male = 1


class SpecieEnum(int, Enum):
    Adelie = 0
    Chinstrap = 1
    Gentoo = 2


class Pinguim(BaseModel):
    """ 
    Atributos de um pinguim 
    """

    island: IslandEnum
    bill_length_mm: int
    bill_depth_mm: int
    flipper_length_mm: int
    body_mass_g: int
    sex: SexEnum
