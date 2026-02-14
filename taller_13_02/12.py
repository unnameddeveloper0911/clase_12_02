#Write a function that counts the number of words in a sentence.

frase="Esta es una frase"

def contarPalabras(frase):
    numPalabras=frase.split()
    return len(numPalabras)

print("El numero de palabras es: ", contarPalabras(frase))