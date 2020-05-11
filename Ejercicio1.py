'''
Created on 11 may. 2020

@author: Guzman Lopez Cesar Gerardo 88-8@live.com.mx
'''
from math import log 
 
import random
vel_arribo=4.0
vel_partida=3.0
total_clientes=10000
ilam=1/vel_arribo
imiu = 1/vel_partida

a=[] #arribo
previo=0.0

b=[]#inicio de servicio

c=[]#fin de sevicio

salida=0.0
d=[]#tiempo en el sistema

suma=0.0 #suma de los tiempos en sistema
print("Nombre")

for i in range(total_clientes):
    inter = -1*ilam*log(random.random())
    a.insert(i%2, previo+inter)
    previo = a[i%2]
    b.insert(i%2, max(salida, a[i%2]))
    serv = -1*imiu*log(random.random())
    c.insert(i%2,b[i%2]+serv )
    salida = c[i%2]
    d.insert(i%2,c[i%2]-a[i%2])
    suma += d[i%2]
    print("__________________________________")
    print("Cliente % 2d " %(i))
    print("llegada % 6.3f"%(a[i%2]))
    print("inicia  % 6.3f"%(b[i%2]))
    print("termina % 6.3f"%(c[i%2]))
    print("permanencia % 6.3f\n"%(d[i%2]))
     
print("\nel tiempo promedio en el sistema es: ",suma/i) 
    
if __name__ == '__main__':
    pass