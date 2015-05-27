
a = -3 
b = 3
h = 0.25
n = 25        -- alterar

x = [a + i * h | i <- [0..n - 1]]
e = realToFrac (exp 1)

f t =
  e ** (- (t ** 2))

y     = map (f) x
xxx   = [ y !! round(i) | i <- [1.. n - 2]]
ab    = map (* 2) xxx
aab   = [y !! 0] ++ ab ++ [y !! round (n - 2)]


final = (2 / sqrt(pi)) * ((h / 2) * sum aab)


