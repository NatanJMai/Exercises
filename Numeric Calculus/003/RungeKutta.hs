  -- Runge Kutta method.
b = 2
a = 0
n = 5
h = 0.4
c = round(n - 1) :: Int
x = [a + (i * h) | i <- [0..n]]

y1 = [2]
y  = ff y1 0

f x y =
    x - y + 2

elemE xs n =
    xs !! n

calcK i yy =
    (elemE yy i) + (1/6) * (a +(2 * b) + (2 * c) + d)
    where a = h * f (elemE x i)(elemE yy i)
          b = h * f ((elemE x i) + (h/2))((elemE yy i) + (a / 2))
          c = h * f ((elemE x i) + (h/2))((elemE yy i) + (b / 2))
          d = h * f ((elemE x i) + (h/2))((elemE yy i) + (c / 2))

ff yy i
  | i           > c   = yy
  | otherwise         = ff a (i + 1)
  where a             = yy ++ [calcK i yy]
