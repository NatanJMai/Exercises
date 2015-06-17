#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math  import exp
from gauss import func

def alpha ():
	return 2 - h

def betha (i):
	return (2 * (i * (h ** 3)) - 4)

def delta ():
	return 2 + h

def res(i):
	return ( ((-2) * (h ** 2)) * (e ** (i * h))) * ((((i * h) ** 2)) + 1)

def main():
	global a, b, h, n, e
	e = exp (1)
	a = 0
	b = 1
	h = 0.1
	n = int((b - a) / h)
	result  = []
	x       = []
	for i in range(0, n + 1):
		x.append(i * h)

	for i in range(0, n):
		result.append(res(i))

	A = alpha()
	D = delta()

	matriz = []

	# Matriz = 0
	for i in range(0 , n - 1):
		matriz.append([0 for i in range (0, n)])

	linhas = n - 1
	colun  = linhas + 1

	#print(linhas)
	#print(colun)

	for i in range(0, linhas):
		for j in range(0, colun):
			if i == j:
				matriz[i][j] = betha(i + 1)
				matriz[i][j - 1] = D
				matriz[i][j + 1] = A

			if j == colun - 1:
				if i == linhas - 1:
					matriz[i][j] = (result[9] - (alpha() * e))
				else:
					matriz[i][j] = result[i + 1]


	novaV  = result
	nova   = func(matriz)


	teste  = [e]
	teste.append(nova[n - 2][n - 1] / nova[n - 2][n - 2])

	#teste[1] = x9
	#teste[2] = x8


	x10	   = e
	x9     = nova[8][9]   / nova[8][8]
	x8     = (nova[7][9]  - (nova[7][8]  * x9)) / nova[7][7]
	x7     = (nova[6][9]  - (nova[6][7]  * x8)) / nova[6][6]
	x6     = (nova[5][9]  - (nova[5][6]  * x7)) / nova[5][5]
	x5     = (nova[4][9]  - (nova[4][5]  * x6)) / nova[4][4]
	x4     = (nova[3][9]  - (nova[3][4]  * x5)) / nova[3][3]
	x3     = (nova[2][9]  - (nova[2][3]  * x4)) / nova[2][2]
	x2     = (nova[1][9]  - (nova[1][2]  * x3)) / nova[1][1]
	x1     = (nova[0][9]  - (nova[0][1]  * x2)) / nova[0][0]
	x0	   = 0

	for i in x:
		print(i)

	print("X0: %f" % x0)
	print("X1: %f" % x1)
	print("X2: %f" % x2)
	print("X3: %f" % x3)
	print("X4: %f" % x4)
	print("X5: %f" % x5)
	print("X6: %f" % x6)
	print("X7: %f" % x7)
	print("X8: %f" % x8)
	print("X9: %f" % x9)
	print("X10: %f" % x10)



if __name__ == "__main__":
	main()
