#se crea un contador en 0
x = 0
#mientras x sea menor a 101
while (x < 101):
# si  es multiplo de 5 y de 3
    if (x % 5) == 0 and (x % 3) == 0:
# imprime valor de fizzbuzz
        print "fizzbuzz"
#a x se le asigna x +1
        x = x + 1
#si x es multiplo de 3
    elif (x % 3) == 0:
#imprime Fizz
        print "Fizz"
#a x se le asigna x +1
        x = x + 1
#si x es multiplode 5
    elif (x % 5) == 0:
#imprime Buzz
        print "Buzz"
#a x se le asigna x +1
        x = x + 1
#sino
    else:
#a x se le asigna x +1
        print x
        x = x + 1
