import psycopg2 as bd

conexion = bd.connect(
    user='postgres',
    password='123456789',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)
try:
    #el valor por defecto sera True
    #conexion.autocommit = False #se debe agregar el autocommit en False para manejar las transacciones

    #cursor = conexion.cursor()
    #sentencia = 'insert into persona (nombre,apellido,email) values (%s,%s,%s)'
    #valores = ('Maria 1','Exparza 1','mesparza 1@mail.com')
    #cursor.execute(sentencia,valores)

    #sentencia = 'update persona set nombre = %s,apellido = %s,email = %s where id_persona = %s'
    #valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com',1)
    # cursor.execute(sentencia,valores)

    #conexion.commit()
    with conexion: #manejo de recursos ya administra el commit y el rollback
        with conexion.cursor() as cursor:
            sentencia = 'update persona set nombre = %s,apellido = %s,email = %s where id_persona = %s'
            valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com',1)
            cursor.execute(sentencia,valores)
except Exception as e:
    #conexion.rollback() #con el with no es necesario agregar esta linea
    print('Error en la Transaccion')
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()
print('Transaccion terminada')