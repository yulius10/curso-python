import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='123456789',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            #sentencia = 'select * from persona where id_persona = %s'
            #id_persona = 1#input("Ingrese el id_persona:")
            #cursor.execute(sentencia,(id_persona,))
            #registro = cursor.fetchone()
            #print(registro)
            #sentencia = 'select * from persona where id_persona in %s'
            sentencia = 'select * from persona'
            #id_persona = input("Ingrese el id_persona:")
            #llaves_primarias = ((1,2),)
            #entradas = input("Ingrese los id\'s a buscar (separado por comas):")
            #llaves_primarias = (tuple(entradas.split(',')),)
            #cursor.execute(sentencia,llaves_primarias)
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for row in registros:
                print(row)

            sentencia = 'insert into persona (nombre,apellido,email) values (%s,%s,%s)'
            valores = (('Carlos 1','Lara 1','clara1@mail.com'),
                       ('Marcos','Cantu','mcantu@mail.com'),
                       ('Angel','Quintana','aquintana@mail.com'),
                       ('Maria','Gonzales','mgonzales@mail.com'))
            #cursor.execute(sentencia,valores)#inserta un solo registro
            #cursor.executemany(sentencia,valores)#inserta varios registro
            #conexion.commit() #esto lo hace automatica con el with
            #registros_insertados = cursor.rowcount
            #print(f"Registros insertados: {registros_insertados}")

            sentencia = 'update persona set nombre = %s,apellido = %s, email = %s where id_persona = %s'
            valores = ('Juan Carlos','Juarez','jcjuarez@mail.com',3)
            #cursor.execute(sentencia, valores)
            #registros_actualizados = cursor.rowcount
            #print(f"Registro actualizado: {registros_actualizados}")

            sentencia = 'update persona set nombre = %s,apellido = %s, email = %s where id_persona = %s'
            valores = (('Juan', 'perez', 'jperez@mail.com', 3),
                       ('Ivon', 'Gutierrez', 'igutierrez@mail.com', 2))
            #cursor.executemany(sentencia, valores)
            #registros_actualizados = cursor.rowcount
            #print(f"Registros actualizados: {registros_actualizados}")

            sentencia = 'delete from persona where id_persona = %s'
            valores = (7,)
            #cursor.execute(sentencia, valores)
            #registros_borradas = cursor.rowcount
            #print(f"Registros eliminados: {registros_borradas}")

            sentencia = 'delete from persona where id_persona in %s'
            valores = ((5,6),)
            #cursor.execute(sentencia, valores)
            #registros_borradas = cursor.rowcount
            #print(f"Registros eliminados: {registros_borradas}")


except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()