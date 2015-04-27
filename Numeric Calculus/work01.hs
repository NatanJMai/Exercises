n  = 5
x  = [0, 0.1, 0.3, 0.6, 1]
y  = [1, 2, 4.1, 8.3, 21]

xi² :: (Floating a ) => [a] -> [a]
xi² xi =
    [x ^ 2 | x <- xi]

yi² :: (Floating a) => [a] -> [a]
yi² yi =
    [y ^ 2 | y <- yi]

somX    = sum(x)
somY     = sum(y)
somX²   = sum (xi² x)
somY²   = sum (yi² y)
somXY  = sum (zipWith (\x y -> x * y) x y)

a = (n * somXY - (somX * somY)) / ((n * somX²) - (somX ^ 2))
b = (somY - (a * somX)) / n
r² = ((somXY - (somX * somY) / n) ^ 2) / ( (somX² - ((somX) ^ 2) / n) * (somY² - (somY ^ 2) / n))



