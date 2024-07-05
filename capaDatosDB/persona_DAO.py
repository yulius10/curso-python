from cursor_pool import cursorPool
from persona import Persona
from logger_base import log

class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create - Read - Update - Delete)
    '''

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona (nombre,apellido,email) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):
        with cursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls,persona):
        with cursorPool() as cursor:
            valores = (persona.nombre,persona.apellido,persona.email)
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f'Persona a insertada: {persona}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with cursorPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with cursorPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto Eliminado: {persona}')
            return cursor.rowcount

if __name__ == '__main__':
    #insertar registro
    #persona1 = Persona(nombre='Pedro',apellido='Najera',email='pnajera@mail.com')
    #personas_insertadas = PersonaDAO.insertar(persona1)
    #log.debug(f'Personas insertadas {personas_insertadas}')

    #actualizar registro
    #persona1 = Persona(1,'Juan 1', 'Perez 1', 'jperez1@mail.com')
    #personas_actualizadas = PersonaDAO.actualizar(persona1)
    #log.debug(f'Personas actualizadas {personas_actualizadas}')

    #eliminar registro
    #persona1 = Persona(id_persona=11)
    #personas_eliminadas = PersonaDAO.eliminar(persona1)
    #log.debug(f'Personas eliminadas {personas_eliminadas}')

    #seleccionar objeto
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
