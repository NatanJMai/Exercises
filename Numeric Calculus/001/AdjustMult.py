from array import *
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

final = [[2,3]      , [xAux[0]], [xAux[1]], [xAux[2]], [xAux[3]], [xAux[4]], [xAux[5]],
        [xAux[0]] , [xAux[1]], [xAux[2]], [xAux[3]], [xAux[4]], [xAux[5]] , [xAux[6]],
        [xAux[1]] , [xAux[2]], [xAux[3]], [xAux[4]], [xAux[5]], [xAux[6]] , [xAux[7]],
        [xAux[2]] , [xAux[3]], [xAux[4]], [xAux[5]], [xAux[6]], [xAux[7]] , [xAux[8]],
        [xAux[3]] , [xAux[4]], [xAux[5]], [xAux[6]], [xAux[7]], [xAux[8]] , [xAux[9]],
        [xAux[4]] , [xAux[4]], [xAux[5]], [xAux[6]], [xAux[7]], [xAux[8]] , [xAux[9]]]


