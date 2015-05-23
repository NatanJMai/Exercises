-- Euler Method
-- Computer Science
-- Natan J. Mai

b = 3
a = 1
h = 0.1
n = (b - a) / h
c = round (n - 1):: Int


f x y =
  (y / x) - (y / x) ^ 2

y = [1]

x = [ a + (i * h) | i <- [0 .. n - 1]]


yi 0 = y !! 0
yi z =
  (y !! (z - 1)) + (h * f (x !! (z - 1))(y !! (z - 1)))


elemE a n =
  a !! n


ff yy i
  | i             > c     = yy
  | otherwise             = ff a (i + 1)
  where a                 = yy ++ [(elemE yy i) + (h * f (elemE x i)(elemE yy i))]



