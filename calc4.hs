import Data.List
import Data.Maybe (fromJust)

{-
    Gauss Method
-}

--calcM :: (Num a , Fractional a, Integral a) =>a -> a -> a
calcM a b =
    a / b

--calculo :: (Num a, Fractional a, Integral a) => [a] -> [a] -> [a]
calculo xs ys ind= do
    zipWith ( \x y -> y - m * x ) xs ys
        where m = calcM (ys !! ind) (xs !! ind)

{-result xs =
    [xs !! 0] ++
    gauss'(gauss xs 1 0 1) 2 1 1-}

rssss xs =
    [xs !! 0] ++
    gauss(gauss xs 1 0 1) 2 1 1


gauss xs k tt jj
    | k                     == 1        = first xs k ++  second xs k tt jj ++ second xs k tt (jj + 1)
    | k                     == 2        = first xs k ++  second xs k tt jj

-- segundo pivo
gauss2 xs k tt jj =
    first xs k ++
    second xs k tt jj

first xs k =
    [[x | x <- xs !! a]]
        where a = k - 1

second xs k tt j =
    [[y |y <- calculo (xs !! a)(xs !! (a + j)) tt ]]
        where a = k - 1

