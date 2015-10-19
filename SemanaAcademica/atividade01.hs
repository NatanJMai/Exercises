{--
- Autor: Natan J. Mai
- natan.mai@hotmail.com
- Universidade Federal da Fronteira Sul
-
- Programação Funcional 
- Semana Acadêmica do curso de Ciência da Computação
--}

at01 :: (Num t, Eq t, Enum t) => t -> [(t, t)]
at01 z = 
  [(x, y) | x <- [0..10], 
        	y <- [0..10], 
         	x + y == z]

at2 = take 3 [1..]
at3 = take 1 (at01 6)

f = map (\x -> x ^ 2) [1, 2, 3]
a = (\x -> x) "Nao tenho nome"
b = (\x -> x ^ 2)
p = sum [2, 3, 4, 5]
c = [x | x <- [1..10], x ^ 2 == 9]

ourmap :: (t -> a) -> [t] -> [a]
ourmap f [] = []
ourmap f (x:xs) = 
    [f x] ++ ourmap f xs


at5  = take 14 [-1..]
at51 = [x * (x ^ 2) | x <- at5]
at52 = sum at51
at60 = sum [x ^ 2 | x <- take 10 [3..]]
at70 = [(x, y, z) | x <- [0..50], y <- [0..50], z <- [0..50],
                    (2 * x) + y -  z       == 1, 
                    (3 * x) - y + (z * 2)  == 7, 
                         x  + y +  z       == 6]

at80 = sum (take 5 [x | x <- [0..], x ^ 2 > 1000])

z = [(x, 2 * x) | x <- [0..9], x ^ 2 == 9]
