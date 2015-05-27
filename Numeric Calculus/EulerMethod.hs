-- Euler Method
-- Computer Science
-- Numeric Calculus
-- Question nr 2 .
-- Natan J. Mai

b    = 3
a    = 1
h    = 0.05
y1   = [1]
n    = (b - a) / h
c    = round (n - 1):: Int
y    = ff y1 0
e    = er [] 0
erro = zipWith (-) y e

f x y =
  (y / x) - (y / x) ^ 2

y' x =
  (x / (1 + log(x)))

x = [ a + (i * h) | i <- [0 .. n]]

elemE a n =
  a !! n

ff yy i
  | i             > c     = yy
  | otherwise             = ff a (i + 1)
  where a                 = yy ++ [(elemE yy i) + (h * f (elemE x i)(elemE yy i))]

er v s
  | s             > c + 1 = v
  | otherwise             = er a (s + 1)
  where a                 = v ++ [y'(elemE x s)]
