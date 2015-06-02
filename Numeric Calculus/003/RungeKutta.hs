-- Runge Kutta method.
b = 2
a = 0
n = 5
h = 0.4
c = 2
x = [a + (i * h) | i <- [0..n]]

y1 = [2]
y  = ff y1 0


f x y = 
    x - y + 2

elemE xs n = 
    xs !! n

k1 i yy = 
    h * f (elemE x i)(elemE yy i)

k2 i yy = 
    h * f ((elemE x i) + (1/2) * h)((elemE yy i) + (1/2) * (k1 i yy)) 

k3 i yy = 
    h * f ((elemE x i) + (1/2) * h) ((elemE yy i) + (1/2) * (k2 i yy))

k4 i yy = 
    h * f ((elemE x i) + (1/2) * h) ((elemE yy i) + (1/2) * (k3 i yy))

calcK i yy =
    (elemE yy i) + (1/6) * (((k1 i yy) + (k2 i yy) + (k3 i yy) + (k4 i yy)))


ff yy i 
  | i           > 1   = yy
  | otherwise         = ff a (i + 1)
  where a             = yy ++ [calcK i yy]
