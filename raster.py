# Algoritmo da Reta de Bresenham

# Reta 1

import matplotlib.pyplot as plt

Xi = 0
Yi = 6
Xf = 10
Yf = 9
Posi = Xi
Posf = Yi
xr =[Posi]
yr =[Posf]
print(str(Posi) + ", " + str(Posf))
while Posi < Xf:
    Dx = Xf - Posi
    Dy = Yf - Posf 
    M = Dy / Dx 
    B = (Yf - (M * Xf)) 
    
    Condição = (Dx*Posi) + (-Dy*Posf) + (Dy * B)
    
    if(Condição > 0):
    
        Posi += 1
        Posf +=1
        
    elif(Condição < 0):   
        Posi += 1

    else:
        
        Posi += 1
        Posf +=1
    xr.append(Posi)
    yr.append(Posf)
    print(str(Posi) + ", " + str(Posf))

# Reta 2

Xi = 0
Yi = 13
Xf = 10
Yf = 22
Posi = Xi
Posf = Yi
xr2 =[Posi]
yr2 =[Posf]
print(str(Posi) + ", " + str(Posf))
while Posi < Xf:
    Dx = Xf - Posi
    Dy = Yf - Posf 
    M = Dy / Dx 
    B = (Yf - (M * Xf)) 
    
    Condição = (Dx*Posi) + (-Dy*Posf) + (Dy * B)
    
    if(Condição > 0):
    
        Posi += 1
        Posf +=1
        
    elif(Condição < 0):   
        Posi += 1

    else:
        
        Posi += 1
        Posf +=1
    xr2.append(Posi)
    yr2.append(Posf)
    print(str(Posi) + ", " + str(Posf))

# =============================================================================

# Algoritmo da circunferência de Bresenham

import math

p1 = 0
p2 = 0

# vetor X de valores
x = []
# vetor Y de valores
y = []

# raio
r = 5
# angulos
theta = []

for k in range(360):
  theta.append(k)

posi = 0
# transformando coordenadas polares em cartesianas
while (posi < 360):

  # x = R * cos(theta)
  p1 = r * math.cos(theta[posi]) + 24
  x.append(round(p1))

  # y = R * sen(theta)
  p2 = r * math.sin(theta[posi]) + 15
  y.append(round(p2))
  
  posi += 1

# =============================================================================

# Algoritmo de visualização do Raster

import numpy as np
import cv2 as cv 
from google.colab.patches import cv2_imshow # for image display
import matplotlib.pyplot as plt

DimRaster=30 #Define o tamanho do raster  
#Criando um raster de cor preta
Raster= np.zeros((DimRaster,DimRaster))  # Na visualização 0 -> Preto  e 255 -> Branco
#forma do array
print("Foi criado um RASTER de tamanho ",Raster.shape)

for ii in range(len(y)):
  Yc= DimRaster - y[ii]
  Raster[Yc,x[ii]]=255

for ii in range(len(yr)):
  Yc= DimRaster - yr[ii]
  Raster[Yc,xr[ii]]=255

for ii in range(len(yr2)):
  Yc= DimRaster - yr2[ii]
  Raster[Yc,xr2[ii]]=255

plt.imshow(Raster,cmap='gray')