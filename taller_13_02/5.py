## Write a function that checks whether a string is a palindrome (reads the same forwards and backwards).
## Consider case sensitivity and ignoring spaces.
def reversa(texto):
    textoComparar = texto.lower()
    return textoComparar == textoComparar[::-1] ## revisa el texto es igual al derecho y al reves
texto = input("Ingrese un texto para saber si es un palindromo: ")
print(reversa(texto))