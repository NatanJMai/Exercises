#!usr/bin/env/python

#------------------------------------------------------------
#   NAME : Natan J. Mai
#   DATE : 17/06/2015
#   FILE : IntegrNumeric.py
#   EMAIL: natan.mai@hotmail.com
#   FUNCT: Description
#------------------------------------------------------------

from math import pi
from math import exp as e
from math import sqrt

def princ(a1, b1, h1):
  global a, b, h, n
  a = a1
  b = b1
  h = h1
  n = int((b - a) / h)
  return calculo()


def f(x):
  return e (- (x ** 2))


def initX():
  x = []
  for i in range(0, n + 1):
    x.append(a + (i * h))
  return x


def initY(x):
  y = []
  for i in range(0, n + 1):
    y.append(f (x[i]))
  return y


def printN(lista, desc):
  print(desc)
  for i in lista:
    print(i)


def fourTwoOne(i):
  if i == 0 or i == n:
    return 1
  elif i % 2 == 0:
    return 2
  else:
    return 4


def final(y):
  y1 = []
  for i in range(0, len(y)):
    y1.append(fourTwoOne(i) * y[i])
  return y1




def calculo():
   x  = initX()
   y  = initY(x)
   y1 = final(y)
   t1 = (h / 3) * (sum(y1))
   t2 = (2 / (sqrt(pi))) * t1

   if __name__ == "__main__":
        printN(x, "X => ")
        printN(y, "\n\nY => ")
        printN(y1, "\n\nY' => ")
        print("\n\nAreaTotal => %f" % t2)

   return y


if __name__ == "__main__":
  princ(-5, 5, 0.125)

