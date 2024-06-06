#---------- EXERCISE #03 ----------#

""" Definir una función que calcule la longitud de una lista o una 
cadena dada. (Es cierto que python tiene la función len() incorporada, 
pero escribirla por nosotros mismos resulta un muy buen ejercicio. """

#%% Empezando el Ejercício:

#Considerando que los números son tipo int:
def contar_chars(string: str):
    x = 0
    for i in string:
        x += 1
    return x
# %% Llamando la Función:

string = "dois"
res = contar_chars(string)
print("En la String:", "(" + string + ")", " Hay:", res, "caracteres.")

# %%
