-- Euler Method
-- Computer Science
-- Natan J. Mai

b = 2
a = 0
n = 5

h = (b - a) / n

f :: (Floating a) => a -> a -> a
f x y = 
   x + y

y = [a]

x = [ a + (i * h) | i <- [0 .. n]]


--yi = yi - 1 + h * f(xi - 1, yi - 1)
