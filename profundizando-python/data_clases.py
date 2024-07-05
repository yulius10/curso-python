from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Persona:
    nombre: str
    apellido: str
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor nombre vacio: {self.nombre} ')

persona1 = Persona('Juan','Perez')
print(f'{persona1}')

#variable de clase
print(Persona.contador_personas)

#variable de instancia
print(f'variable de instancia: {persona1.__dict__} {persona1.apellido}')

persona2 = Persona(nombre='aaa',apellido='Perez')
print(f'persona vacia: {persona2}')

