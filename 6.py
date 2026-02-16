## Write a program that prints numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number,
## and for multiples of 5, print "Buzz". For numbers which are multiples of both 3 and 5, print "FizzBuzz".
def mult(num):
    if num % 3 == 0 and num % 5 == 0: ## por cuestiones de funcionalidad es mejor que
        print("FizzBuzz")             ## primero esté el fizzbuzz
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else: print(num)
for i in range(101): ## es 101 porque el i va hasta el rango -1
    mult(i)


