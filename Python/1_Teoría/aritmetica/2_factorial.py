import math

def factorial(n:int)->int:
    fac=1
    
    for i in range(1,n+1):
        fac=fac*i
        #tambien fac*=i

    return fac

#Se invoca un Print para comprobar con un ejemplo si funciona
print(factorial(5))