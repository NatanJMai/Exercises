#!/usr/bin/env python
# Gauss Method

def func(matriz):

    #matriz  = [[8,22,8,57],[22,108,57,92],[8,57,36,-5]]'''

    #matriz = [[1,6,2,4,8], [3,19,4,15,25], [1,4,8,-12,18],[5,33,9,3,72]]
    #matriz = [[3, 4, 5, 7, 20],[2, 1, 3, 0, 11],[1, 2, 3, 4, 10],[2, 2, 2, 2, 10]]
    #pivos  = [1, -3, -1]

    linhas  = len(matriz)
    colunas = linhas + 1

    for pivo in range(0,linhas):
        for linhasAb in range(pivo + 1, linhas):
            m = float(matriz[linhasAb][pivo]) / float(matriz[pivo][pivo])

            for elemento in range(pivo,colunas):
                a = float(round(matriz[linhasAb][elemento], 2)) - float(round((m * matriz[pivo][elemento]), 10))
                matriz[linhasAb][elemento] = round(a, 10)

    return matriz

if __name__ == '__main__':
    matriz = [
                    [-3.998, 1.9, 0, 0, 0, 0, 0, 0, 0, -0.022324452545128087],
                    [2.1, -3.996, 1.9, 0, 0, 0, 0, 0, 0, -0.025405177369731538],
                    [0, 2.1, -3.994, 1.9, 0, 0, 0, 0, 0, -0.029426922005156876],
                    [0, 0, 2.1, -3.992, 1.9, 0, 0, 0, 0, -0.034610332985277485],
                    [0, 0, 0, 2.1, -3.99, 1.9, 0, 0, 0, -0.041218031767503216],
                    [0, 0, 0, 0, 2.1, -3.988, 1.9, 0, 0, -0.04956163137062186],
                    [0, 0, 0, 0, 0, 2.1, -3.986, 1.9, 0, -0.06000983068262022],
                    [0, 0, 0, 0, 0, 0, 2.1, -3.984, 1.9, -0.07299774245455296],
                    [0, 0, 0, 0, 0, 0, 0, 2.1, -3.982, -5.253773106696067]]

    func(matriz)
