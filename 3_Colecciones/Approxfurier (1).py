import math as m
import numpy as np
import matplotlib.pyplot as plt
a_0=3*m.pi/4 #valor de a_0
p=50 #Numero dado de "n"
#Arreglos para almacenar los datos correspondientes
x=np.arange(-m.pi,m.pi,0.1) #Linspace del Dominio
xn=np.zeros(len(x)*p)
fx=np.zeros(len(x))
fy=np.zeros(len(x))
cn=np.zeros(len(x)*p)
phi=np.zeros(len(x)*p)
aux=0
#Ciclo for principal
for j in range(1,len(x),1):
  suma=0 #Acumulador de suma
  for n in range(1,p+1,1):
      #Calculos de parametros
      an=(1/(m.pi*m.pow(n,2)))*((1-m.pow(-1, n)))
      bn=(m.pow(-1, n+1))/n
      cn[aux]=(m.pow(m.pow(an, 2)+m.pow(bn, 2), 0.5))/2
      if(an==0):
          phi[aux]=m.atan(m.inf)
      elif(an!=0):
          phi[aux]=m.atan(-1*bn/an)
      aux=aux+1
      xn[j]=n
      suma=suma+an*m.cos(n*x[j])+bn*m.sin(n*x[j])
  fx[j]=a_0+suma
  if(x[j]<0):
      fy[j]=x[j]+m.pi
  elif(x[j]>0):
      fy[j]=m.pi
#Graficas
#plt.hist(cn, x)
plt.plot(x,fx)
plt.plot(x,fy)
