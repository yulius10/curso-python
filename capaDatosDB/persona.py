import logging
from logger_base import log

class Persona:
    def __init__(self,id_persona:int=None,nombre:str=None,apellido:str=None,email:str=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'''
            ID_Persona: {self._id_persona},
            Nombre: {self._nombre},
            Apellido: {self._apellido},
            Email: {self._email}
        '''
    @property
    def id_persona(self)->int:
        return self._id_persona

    @id_persona.setter
    def id_persona(self,id_persona:int)->None:
        self._id_persona = id_persona

    @property
    def nombre(self)->str:
        return self._nombre

    @nombre.setter
    def nombre(self,nombre:str)->None:
        self._nombre = nombre

    @property
    def apellido(self)->str:
        return self._apellido

    @apellido.setter
    def apellido(self,apellido:str)->None:
        self._apellido = apellido

    @property
    def email(self)->str:
        return self._email

    @email.setter
    def email(self,email:str)->None:
        self._email = email


if __name__ == '__main__':
    persona1 = Persona(1,'Juan','Perez','jperez@mail')
    log.debug(persona1)
    #simular un insert
    persona2 = Persona(nombre='Maria',apellido='Castrezano',email='mcastrezano@mail.com')
    log.debug(persona2)
    #simular un delete
    persona3 = Persona(id_persona=3)
    log.debug(persona3)