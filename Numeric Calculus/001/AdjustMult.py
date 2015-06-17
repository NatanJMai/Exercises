#!usr/bin/env/python

import IntegrNumeric

def impressao(lista, descr):
	print(descr)
	for i in lista:
		print(i)

	print("\n")

def main():
	a = -5
	b = 5
	h = 0.125
	n = (b - a) / h
	y = IntegrNumeric.princ(a, b, h)
	x = [a + (i * h) for i in range(0, int(n + 1))]

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

	gass = gauss(finalX)
	x5   = gass[5][6] / gass[5][5]
	x4   = (gass[4][6] - gass[4][5]) / gass[4][4]
	x3   = (gass[3][6] - (gass[3][5] * x5)) / gass[3][3]
	x2   = (gass[2][6] - (gass[2][4] * x4)) / gass[2][2]
	x1   = (gass[1][6] - (gass[1][5] * x5) - (gass[1][3] * x3)) / gass[1][1]
	x0   = (gass[0][6] - (gass[0][4] * x4) - (gass[0][2] * x2)) / gass[0][0]
	beta = [x0, x1, x2, x3, x4, x5]

	soma = 0
	yBarr = []

	for i in range(0,len(x)):
		yBarr.append((beta[0] + (beta[1] * x[i]) + (beta[2] * (x[i] ** 2)) + (beta[3] * (x[i] ** 3)) + (beta[4] * (x[i] ** 4)) + (beta[5] * (x[i] ** 5))))
		soma = soma + ((y[i] - (beta[0] + beta[1] * x[i] + (beta[2] * (x[i] ** 2)) + (beta[3] * (x[i] ** 3)) + (beta[4] * (x[i] ** 4)) + (beta[5] * (x[i] ** 5)))) ** 2)

	baixo  = sum_y2 - (((sum_y) ** 2) / n)
	r2     = 1 - (soma / baixo)

	print("B = %s" % beta)
	print("R2: %f" % r2)

	impressao(x, "-----------------------X--------------------")
	impressao(y, "-----------------------Y--------------------")
	impressao(yBarr, "-----------------------R--------------------")



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
