#Write a program that prints a right-angled triangle pattern with a given number of rows.

numFilas=int(input("Ingrese el numero de filas: "))
salida=[]
i=0
while i < numFilas:
    i+=1
    salida.append('* ')
    print(salida)