#Write a function that takes a string as input and returns the number of vowels and consonants in the string.

palabra="Stratocaster"

def contarVocales(palabra):
    vocales=0
    for i in palabra:
        if i in "aeiouAEIOU":
            vocales+=1
    return vocales

def contarConsonantes(palabra):
    consonantes=0
    for i in palabra:
        if i not in "aeiouAEIOU":
            consonantes+=1
    return consonantes

print("El numero de vocales es: ", contarVocales(palabra))
print("El numero de consonantes es: ", contarConsonantes(palabra))