# fibonacci.py
#Definicion de la funcion
def fib(i):
# se crea una variable a = 0
      a = 0
# se crea una variable b = 1    
      b = 1
# se crea una variable c = 0   
      c = 0
#mientras c sea menor a i
      while c < i:
#imprime variable c      
            print c, 
# a la variable a se le asigna la variable b
            a = b
# a la variable b se le asigna la variable c
            b = c
# a la variable c se le asigna la suma de a+b
            c = a+b
#Llamamos a la funcion  ftb hasta 1000000 
fib(1000000) 
