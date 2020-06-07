'''
Created on 30 may. 2020

@author: Guzman Lopez Cesar Gerardo 88-8@live.com.mx

En una estacion de policia de una ciudad grande, 
se reciben 4 llamadas telefonicas por minuto en promedio.
Asuma que el tiempo que pasa entre una llamada y otra tiene
una distribucion exponencial. 
Tome en cuenta que solamente nos importa 
la velocidad con la que entran las llamadas, 
e ignoramos el tiempo que duran las llamadas. 
Tambien vamos a asumir que el tiempo transcurrido 
entre llamadas es independiente.
Entonces podemos deducir que el numero total de
 llamadas recibidas durante un periodo 
 de tiempo tiene una distribucion de Poisson

'''
from math import e,factorial
 
#lamda = es un parametro positivo que representa el numero de 
#        veces que se espera que ocurra el fenomeno durante un intervalo dado
#i=
def Poisson(lambda_1, i):
    return  ((e**(-lambda_1)) * lambda_1**i)/factorial(i)

print("Pregunta 2.- ", Poisson(2/3, 1))
print("Pregunta 3.- ", Poisson(4, 5))
#pregunta 4 probabilidad acumulada
prob_5=0
for i in range(5):
    prob_5+=Poisson(4,i)
print("Pregunta 4.- ", Poisson(4, i))
#pregunta 5
prob_mas_40=0
for i in range(40):
    prob_mas_40+=Poisson(8*4,i)
print("Pregunta 5.- ",1.0-prob_mas_40)