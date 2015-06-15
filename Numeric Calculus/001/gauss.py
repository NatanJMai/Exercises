#!/usr/bin/env python
# Gauss Method

def main():
    matriz  = [[8,22,8,57],[22,108,57,92],[8,57,36,-5]]
    #matriz = [[1,6,2,4,8], [3,19,4,15,25], [1,4,8,-12,18],[5,33,9,3,72]]
    #matriz = [[3, 4, 5, 7, 20],[2, 1, 3, 0, 11],[1, 2, 3, 4, 10],[2, 2, 2, 2, 10]]
    #pivos  = [1, -3, -1]

    linhas  = len(matriz)
    colunas = linhas + 1

    for pivo in range(0,linhas):
        for linhasAb in range(pivo + 1, linhas):
            m = float(matriz[linhasAb][pivo]) / float(matriz[pivo][pivo])

            for elemento in range(pivo,colunas):
                a = float(round(matriz[linhasAb][elemento], 2)) - float(round((m * matriz[pivo][elemento]), 2))
                matriz[linhasAb][elemento] = round(a, 2)

    print(matriz)

if __name__ == '__main__':
    main()
