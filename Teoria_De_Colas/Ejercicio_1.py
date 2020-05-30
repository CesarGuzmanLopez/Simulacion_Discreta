'''
Created on 30 may. 2020

@author: Guzman Lopez Cesar Gerardo 88-8@live.com.mx

Supongamos que a una sucursal bancaria estan llegando clientes con una velocidad 
promedio de 4.5 por minuto. Queremos saber,
cual es la probabilidad de que en el proximo minuto lleguen 0, 1, 2 o i clientes?

En una tabla, muestre los calculos para i=0, 1, 2, 3, 4 y 5 con 6 intervalos de 10 segundos.
Luego calcule las probabilidades para i=0, 1, 2, 3, 4 y 5 con 10 intervalos de 6 segundos.
Finalmente repita los calculos para i=0, 1, 2, 3, 4 y 5 con 20 intervalos de 3 segundos.


 
'''

from math import factorial
 
 
def combinatoria(n,i):
    return (1.0*factorial(n))/(factorial(i)*factorial(n-i))

def Probabilidad_de_evento_i(n,p,i): 
    '''
    n = numero total de eventos independientes a considerar
    
    i = i es el numero de ocurrencias del evento o
        fenomeno (la funcion nos da la probabilidad de que el 
        evento suceda precisamente i veces).
             
    p = probabilidad por evento de que suceda el fenomeno
     '''
    q=1-p
    return combinatoria(n, i)*(p**i)*(q**(n-i))


lamda = 4.5 #por minutos 
print("No.inter\t.6\t\t10\t\t20")
for i in range(6):
    print("i:", i,end="")
    for intervalo in [6,10,20]:
        P= Probabilidad_de_evento_i(intervalo, lamda/intervalo, i)
        print("\tP=","{:.10f}".format(P),end="")
    print(" ")