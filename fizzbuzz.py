
x = 0                                       #se crea un contador en 0
while (x < 101):                            #mientras x sea menor a 101 
    if (x % 5) == 0 and (x % 3) == 0:       #si  es multiplo de 5 y de 3
        print x                             #imprime valor de x
        x= x +1                             #a x se le asigna x +1
    elif (x % 3) == 0:                      #si x es multiplo de 3
        print "Fizz"                        #imprime Fizz
        x = x + 1                           #a x se le asigna x +1
    elif (x % 5) == 0:                      #si x es multiplode 5
        print "Buzz"                        #imprime Buzz
        x =x+1                              #a x se le asigna x +1
    else:                                   #sino
        x = x+ 1                            #a x se le asigna x +1
