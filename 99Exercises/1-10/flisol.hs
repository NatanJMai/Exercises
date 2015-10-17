
flisol :: Float -> Float
flisol x =
    (x / 2) * 4

prints :: Show x => x -> IO()
prints x =
   print x


-- Design Pattern
plus :: Num s => [s] -> [s]
plus []     = []
plus (x:xs) =
    x + 1 : plus xs

-- Soma do quadrado dos números naturais menores que 10
a = sum [x ^ 2 | x <- [1..10]]

-- Soma dos cinco primeiros números, tal que seu quadrado seja maior que 1000
c = sum (take 5 [x | x <- [1..], x ^ 2 > 1000])

-- Soma dos números ímpares entre 1 e 300
d = sum( filter odd [1..300])
e = sum( [1,3..300])

-- Soma dos 20 primeiros múltiplos de 13
f = sum(take 2 [13, 26 ..])

-- Tupla (x,y,z), com x, y, z <= 50 tal que
-- 2x + y - z   = 1
-- 3x - y + 2z  = 7
-- x  + y + z   = 6
g = [(x,y,z) |  x <- [1..50], y <- [1..50], z <- [1..50],
                (2 * x) + y - z     == 1,
                (3 * x) - y + 2 * z == 7,
                x + y + z           == 6]

-- Números divisíveis por 3 entre 1 e 100
h = filter p [1..100]
        where p x = x `mod` 3 == 0


ab =[(x, y, z) | x <-[0..50], y <- [0..50], z <-[0..50],
            (2 * x + y - z)        == 1,
            (3 * x - y + 2 * z)    == 7,
            (x + y + z)            == 6]


fat :: (Num a, Eq a) => a -> a
fat 0 = 1
fat x =
    x * fat (x - 1)









