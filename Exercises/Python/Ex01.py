#---------- EXERCISE #01 ----------#

""" Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos. (Es cierto que python tiene una función max()
 incorporada, pero hacerla nosotros mismos es un muy buen ejercicio. """

#%% Empezando el Ejercício:

#Considerando que los números son tipo int:
def calcular_maximo(x: int, y: int) -> int:

    """ Función Para Calcular el Máximo Entre 2 Números """

    if x > y:
        return x
    else:
        return y

#%% 

#Llamar a la Función:
res = calcular_maximo(1, 3)
print("El mayor de los números es:", res)

# %%
