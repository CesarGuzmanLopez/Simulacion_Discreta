'''
Created on 24 may. 2020

@author: Guzman Lopez Cesar Gerardo 88-8@live.com.mx
'''
from random import  random
import matplotlib.pyplot as plt
from math import log

#x = (-1/lambda)*log(1-random())
lambda_=4.5
datos=[int((-1/lambda_)*log(1-random())*100) for _ in range(3000)]
plt.hist(datos, 20, edgecolor='black', linewidth=1)
plt.ylabel("frecuencia")
plt.xlabel("valores")
plt.title("histograma")
plt.show()






if __name__ == '__main__':
    pass