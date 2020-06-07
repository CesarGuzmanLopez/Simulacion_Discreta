'''
Created on 6 jun. 2020

@author: Guzman Lopez Cesar Gerardo 88-8@live.com.mx
'''
from math import log 
import random

def N_N_1(vel_arribo=3.0,vel_partida=5.0,total_Clientes=300,output =True):
   
    ilam=1/vel_arribo
    imiu=1/vel_partida
    
    a=[]
    previo =0.0
    b=[] #inicio de servicio
    salida=0
    c=[]
    
    d=[]
    suma=0.0
    
    
    for i in range(total_Clientes): 
        
       
        inter = -1*ilam*log(random.random())
    
        
        a.insert(i%2, previo+inter)
        previo=a[i%2] 
       
        b.insert(i%2, max(salida,a[i%2])) 
        serv =-1*imiu*log(random.random())
       
        c.insert(i%2, (b[i%2])+serv)
        d.insert(i%2,   c[i%2]-a[i%2]) 

        salida = c[i%2] 
        suma    +=  d[i%2]
        if(output):
            print("Cliente     % 2d" %(i)),
            print("Llegada     % 6.3f"%(a[i%2])),
            print("Inicia      % 6.3f"%(b[i%2])),
            print("Termina     % 6.3f"%(c[i%2])),
            print("Permanencia % 6.3f"%(d[i%2])),
            print("________________________________\n")
    return (suma/total_Clientes)
if __name__ == '__main__':    
    print("\nEn el tiempo en el sistema es de N_N_1: ",N_N_1() )