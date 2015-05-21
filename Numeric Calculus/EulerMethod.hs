-- Euler Method
-- Computer Science
-- Natan J. Mai

b = 1
a = 0
n = 0.1

h = (b - a) / n

f x y = 
    x - y + 2


y = [f a 0]

x = [ a + (i * n) | i <- [0 .. h]]

{--

y1 = y0 + h * f(x0, y0)
y2 = y1 + h * f(x1, y1)
y3 = y2 + h * f(x2, y2) --}

yi 0 = y !! 0
yi z = 
    (y !! (z - 1)) + (n * f (x !! (z - 1))(y !! (z - 1)))

     
--let bb = [ y ++ form i | i <- [1..h]]

elemE a n = 
    a !! n

ff yy i 
    | i                 > 1 	= yy
    | otherwise			= a ++ (ff a (i + 1)) 
    where a 			= yy ++ [(elemE yy i) * h] 
   




--yi = yi - 0 + h * f(xi - 1, yi - 1)
