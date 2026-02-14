#Write a function that checks if two words are anagrams. That is, if they contain the same letters in the
#same quantities, but in a different order. Example: listen and silent

palabra1="casa"
palabra2="saca"

def comparar(palabra1,palabra2):
    lista1 = list(palabra1)
    lista2 = list(palabra2)

    lista1.sort()
    lista2.sort()

    pos = 0
    coincide = True

    while pos < len(palabra1) and coincide:
        if lista1[pos]==lista2[pos]:
            pos = pos + 1
        else:
            coincide = False

    return coincide

if comparar(palabra1,palabra2)==True:
    print("Las palabras son anagramas")
else:
    print("Las palabras no son anagramas")