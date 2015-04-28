n  = 31
x  = [1..31]
y  = [11.7, 12.6, 12.6, 13.8, 15.3, 15  ,
      15.3, 16.9, 16.8, 20.3, 22.2, 20.8,
      19.1, 20.2, 21.2, 23.8, 24.8, 25.4,
      25.9, 26.2, 26.7, 27.8, 28.5, 28.9,
      27  , 25.8, 26.3, 25.2, 26.4, 27  , 26.2]

-- Retorna o quadrado dos valores na lista X.
xi² :: (Floating a ) => [a] -> [a]
xi² xi =
    [x ^ 2 | x <- xi]

-- Retorna o quadrado dos valores na lista Y.
yi² :: (Floating a) => [a] -> [a]
yi² yi =
    [y ^ 2 | y <- yi]

somX   = sum(x)                              -- Soma dos valores na lista X.
somY   = sum(y)                              -- Soma dos valores na lista Y.
somX²  = sum (xi² x)                         -- Soma dos quadrados de X.
somY²  = sum (yi² y)                         -- Soma dos quadrados de Y.
somXY  = sum (zipWith (\x y -> x * y) x y)   -- Multiplicação dos valores de X, Y

-- Fórmula de a
a   = (n * somXY - (somX * somY)) / ((n * somX²) - (somX ^ 2))

-- Fórmula de b
b   = (somY - (a * somX)) / n

-- Fórmula de r²
r²  = ((somXY - ((somX * somY) / n)) ^ 2) / ( (somX² - ((somX) ^ 2) / n) * (somY² - ((somY ^ 2) / n)))

