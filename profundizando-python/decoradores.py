#decoradores
# un decorador es una funcion que recibe una funcion y retorna otra
# lo utilizamos para extender funcionalidades
# 1. Funcion decorador:
# 2. Funcion a decorar
# 3. Funcion decorada


def funciondecorador_a(funcion_a_decorara_b):
    def funcion_decorada_c():
        print('a')
        funcion_a_decorara_b()
        print('c')
    return funcion_decorada_c

@funciondecorador_a
def mostrarMesanje():
    print('Hola desde funcion mensaje')

mostrarMesanje()