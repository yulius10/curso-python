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
            sentencia = 'select * from persona where id_persona in %s'
            #id_persona = input("Ingrese el id_persona:")
            llaves_primarias = ((1,2),)
            #entradas = input("Ingrese los id\'s a buscar (separado por comas):")
            #llaves_primarias = (tuple(entradas.split(',')),)
            cursor.execute(sentencia,llaves_primarias)
            registros = cursor.fetchall()
            for row in registros:
                print(row)

            sentencia = 'insert into persona (nombre,apellido,email) values (%s,%s,%s)'
            valores = ('Carlos','Lara','clara@mail.com')
            cursor.execute(sentencia,valores)
            #conexion.commit() #esto lo hace automatica con el with
            registros_insertados = cursor.rowcount
            print(f"Registros insertados: {registros_insertados}")
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()