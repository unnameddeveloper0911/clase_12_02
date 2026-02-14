#Write a function that takes a text as input and returns a dictionary with the count of how many times each 
#word appears in the text. Ignore case sensitivity.

frase = "hola hola mundo mundo"
diccionario = {}
def contar(frase):
    palabras = frase.split()
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    
    return diccionario
print(contar(frase))