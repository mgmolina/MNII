import numpy as np
from math import sqrt
from matplotlib import pyplot as pp
import cProfile, pstats, StringIO

pr = cProfile.Profile()
pr.enable()
'''
ESTE CODIGO IMPLEMENTA EL METODO DE EULER
Lic Maria Graciela Molina

El metodo de euler es un metodo de un paso de orden 1
Su ecuacion de recurrencia es:
yn+1=yn+hf(xn,yn)
 
*****************************************
Input:
(a,ya): condicion inicial
b: valor en el cual se desea estimar el valor de y
h: valor del paso
'''
def f(t,y):
    '''La funcion f toma como argumentos un par de valore x,y 
    y retorna el valor de la funcion f(x,y)
    '''
    return 1+sqrt(t-y)

def yreal(x):
    return x+1/(1-x)
def graficar(x,y):
    pass

# a y b son los limites del integrador de euler
#N=num de puntos 
a=2
ya=1
b=3
h=0.25
N=(b-a)/h
x = np.linspace(a, b, N+1)
y=yreal(x)

yaprox=np.zeros(N+1)
yaprox[0]=ya
elocal=np.zeros(N+1)
elocal[0]=0

for i in range(1,int(N+1)):
   yaprox[i]=yaprox[i-1]+h*f(x[i-1],yaprox[i-1])
   elocal[i]=abs(yaprox[i]-yaprox[i-1])
   
eglobal=abs(yaprox-y)

#print x
#print y
#print yaprox
#print elocal
#print eglobal
#pp.plot(x,y,'b',x,yaprox,'r',x,eglobal,'k--',x,elocal,'c--',linewidth=2.0)
#pp.title("RK1 - Euler ")
#pp.ylabel("Y",fontsize=16, color='blue')
#pp.xlabel("t",fontsize=16, color='blue')
#pp.show()

pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()


