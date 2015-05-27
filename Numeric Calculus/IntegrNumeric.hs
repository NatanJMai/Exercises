
a = -3 
b = 3
h = 0.25
n = 25        -- alterar

x = [a + i * h | i <- [0..n - 1]]
e = realToFrac (exp 1)

f t =
  e ** (- (t ** 2))

y = map (f) x

y' c indice
  | indice `mod` 2    == 0  = 2 * c
  | otherwise               = c




ab = zipWith (\i j -> if round(i) `mod` 2 == 0 then 2 * j else j) [0 .. n - 1] y
