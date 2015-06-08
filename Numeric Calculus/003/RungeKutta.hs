b = 3
a = 1
n = 8 
h = 0.25
c = round(n - 1) :: Int
x = [a + (i * h) | i <- [0..n]]


k1 = []
k2 = []
k3 = []
k4 = []

y1 = [1]
y  = ff y1 0


k1' x y i = 
    h * f (elemE x i) (elemE y i)

k2' x y i = 
    h * (f (elemE x i + (h * 0.5)) (elemE y i + (0.5 * k1' x y i)))

k3' x y i = 
    h * (f (elemE x i + (h * 0.5)) (elemE y i + (0.5 * k2' x y i)))

k4' x y i =   
    h * (f (elemE x i + (h * 0.5)) (elemE y i + (0.5 * k3' x y i)))

f x y = (y / x) - ((y / x) ^ 2)

elemE xs n = xs !! n

calcK i yy =
        (elemE yy i) + (1/6) * (a +(2 * b) + (2 * c) + d)
            where a = k1' x yy i 
                  --h * f (elemE x i)(elemE yy i)
                  b = k2' x yy i 
                  --h * f ((elemE x i) + (h/2))((elemE yy i) + (a / 2))
                  c = k3' x yy i 
                  --h * f ((elemE x i) + (h/2))((elemE yy i) + (b / 2))
                  d = k4' x yy i 
                  --h * f ((elemE x i) + (h/2))((elemE yy i) + (c / 2))

ff yy i
  | i           > c   = yy
  | otherwise         = ff a (i + 1)
  where a             = yy ++ [calcK i yy]
