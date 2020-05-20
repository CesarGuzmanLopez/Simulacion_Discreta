'''
Created on 18 may. 2020

@author: Guzman Lopez Cesar Gerardo 88-8@live.com.mx
'''
from random  import random
from cmath import sqrt 
aciertos,num_lanzamientos=0.0,5000000
for n in range(num_lanzamientos):aciertos +=(sqrt((random()**2)+(random()**2)).real<=1)
print(" aciertos= ",aciertos," pi= ",4*aciertos/num_lanzamientos)