'''
Created on 6 jun. 2020

@author: Guzman Lopez Cesar Gerardo 88-8@live.com.mx



2 serivdores al desocuparse uno es el que atendera la cola de espera
'''
from math import log 
import random
from Teoria_De_Colas_2.Prog1 import N_N_1

def N_N_2(vel_arribo=3.0,vel_partida=5.0,total_Clientes=300,output =True):
    ilam=1/vel_arribo
    imiu=1/vel_partida
    
    a=[]
    previo =[0,0]
    
    b=[] #inicio de servicio
    salida=[0,0]
    
    c=[]
    d=[]
    suma=[0,0]
    
    for i in range(total_Clientes):
        p =  0 if((salida[0]<salida[1])) else 1 #quien esta atendiendo todavia 
        inter = -1*ilam*log(random.random())  
        a.insert(i%2, previo[p]+inter)#momento en el que llego
        previo[p]=a[i%2]
        b.insert(i%2, max(salida[p],a[i%2]))
        serv =-1*imiu*log(random.random())
        c.insert(i%2, (b[i%2])+serv)
        d.insert(i%2,  c[i%2]-a[i%2]) 
        salida[p] = c[i%2] 
        suma [p]   +=  d[i%2]
        if(output):
            print("Servidor:   % 2d"%(p))
            print("Cliente     % 2d" %(i)),
            print("Llegada     % 6.3f"%(a[i%2])),
            print("Inicia      % 6.3f"%(b[i%2])),
            print("Termina     % 6.3f"%(c[i%2])),
            print("Permanencia % 6.3f"%(d[i%2])),
            print("________________________________\n")
    return max(suma)/total_Clientes;
if __name__ == '__main__':  
    a=  N_N_2()
    b=  N_N_1(output=False)
    print("\nEn el tiempo en el sistema para N_N_2 es: ",a )
    print("En el tiempo en el sistema para N_N_1 es: ",b )
    '''
        Tiempo de ciclo = 
        Trabajo en el proceso / 
        Tiempo promedio que vamos a tardar en terminar
    '''
    trabajo_a= a/(8)
    trabajo_b= b/(8)
    print("trabajo en a: ",trabajo_a)
    print("trabajo en b: ",trabajo_b)