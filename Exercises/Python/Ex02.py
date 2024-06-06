#---------- EXERCISE #02 ----------#

""" Definir una función max_de_tres(), que tome tres números 
como argumentos y devuelva el mayor de ellos. """

#%% Empezando el Ejercício:

#Considerando que los números son tipo int:
def calcular_maximo(x: int, y: int, z: int) -> int:

    """ Función Para Calcular el Máximo Entre 3 Números """

    if x > y and x > z:
        return x
    elif  y > z:
        return y
    else:
        return z

#%% 

#Llamar a la Función:
res = calcular_maximo(10, 8, 5)
print("El mayor de los números es:", res)

# %%