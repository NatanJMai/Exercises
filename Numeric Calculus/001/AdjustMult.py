#!usr/bin/env/python

def main():
  a = -3
  b = 3
  h = 0.25
  n = (b - a) / h 
  x = [a + (i * h) for i in range(0, int(n + 1))] 

  y = [0.000123409804087 , 0.000519574682155, 0.00193045413623, 0.00632971542749  , 0.0183156388887, 
       0.046770622384    , 0.105399224562   , 0.209611387151  , 0.367879441171    , 0.569782824731 , 
       0.778800783071    , 0.939413062813   , 1.0             , 0.939413062813    , 0.778800783071 , 
       0.569782824731    , 0.367879441171   , 0.209611387151  , 0.105399224562    , 0.046770622384 , 
       0.0183156388887   , 0.00632971542749 , 0.00193045413623, 0.000519574682155 , 0.000123409804087]

  xA = [x]
  xA.append([i ** 2 for i in x])
  xA.append([i ** 3 for i in x])
  xA.append([i ** 4 for i in x])
  xA.append([i ** 5 for i in x])
  xA.append([i ** 6 for i in x])
  xA.append([i ** 7 for i in x])
  xA.append([i ** 8 for i in x])
  xA.append([i ** 9 for i in x])
  xA.append([i ** 10 for i in x])

  xAux = map(lambda x: sum(x), xA)

  sum_y   = sum(y)
  sum_y2  = sum(map(lambda y: y ** 2, y))
  sum_xy  = sum(map(lambda x, y: x * y, x, y))
  sum_x2y = sum(map(lambda x, y: (x ** 2) * y, x, y))
  sum_x3y = sum(map(lambda x, y: (x ** 3) * y, x, y))
  sum_x4y = sum(map(lambda x, y: (x ** 4) * y, x, y))
  sum_x5y = sum(map(lambda x, y: (x ** 5) * y, x, y))

  finalX = [[n      , xAux[0], xAux[1], xAux[2], xAux[3], xAux[4] , sum_y  ] ,  
           [xAux[0] , xAux[1], xAux[2], xAux[3], xAux[4], xAux[5] , sum_xy ] , 
           [xAux[1] , xAux[2], xAux[3], xAux[4], xAux[5], xAux[6] , sum_x2y] , 
           [xAux[2] , xAux[3], xAux[4], xAux[5], xAux[6], xAux[7] , sum_x3y] , 
           [xAux[3] , xAux[4], xAux[5], xAux[6], xAux[7], xAux[8] , sum_x4y] , 
           [xAux[4] , xAux[5], xAux[6], xAux[7], xAux[8], xAux[9] , sum_x5y]] 

  ass = gauss(finalX)
  x5  = ass[5][6] / ass[5][5]
  x4  = (ass[4][6] - ass[4][5]) / ass[4][4]
  x3  = (ass[3][6] - (ass[3][5] * x5)) / ass[3][3]
  x2  = (ass[2][6] - (ass[2][4] * x4)) / ass[2][2]
  x1  = (ass[1][6] - (ass[1][5] * x5) - (ass[1][3] * x3)) / ass[1][1]
  x0  = (ass[0][6] - (ass[0][4] * x4) - (ass[0][2] * x2)) / ass[0][0]
  beta  = [x0, x1, x2, x3, x4, x5]
   
  soma = 0
  for i in range(0,len(x)):
    soma = soma + ((y[i] - (beta[0] + beta[1] * x[i] + beta[2] * x[i] + beta[3] * x[i] + beta[4] * x[i] + beta[5] * x[i])) ** 2) 

  baixo  = sum_y2 - ((sum_y) / n)
  r2     = 1 - (soma / baixo)
  print("b = %s" % beta) 


def gauss(matriz):
  linhas  = len(matriz)
  colunas = linhas + 1

  for pivo in range(0, linhas):
    for linhasAb in range(pivo + 1, linhas):
      m = float(matriz[linhasAb][pivo]) / float(matriz[pivo][pivo])

      for elemento in range(pivo, colunas):
        a = float(round(matriz[linhasAb][elemento], 2)) - float(round((m * matriz[pivo][elemento]), 2))
        matriz[linhasAb][elemento] = round(a, 2)
  
  return matriz



if __name__ == "__main__":
  main()
