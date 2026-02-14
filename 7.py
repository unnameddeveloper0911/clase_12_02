##Write a function that calculates the sum of digits of a given integer. For example, the sum of digits
##of 123 would be 1 + 2 + 3 = 6.
def sumaDigitos(numero):
    total = 0
    while numero > 0:
        total += numero % 10
        numero //= 10
    return total
print(sumaDigitos(int(input("ingrese un numero: "))))