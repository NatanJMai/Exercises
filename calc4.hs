import Data.List
import Data.Maybe (fromJust)

{-
    Gauss Method
-}

list :: (Num a) => [[a]]
list =
    [
        [2, 3, (-1), 5],
        [4, 4, (-3), 3],
        [2, -3, 1, (-1)]]


calcM :: (Fractional a) => a -> a -> a
calcM ayx axx =
    ayx / axx

-- l2 = l2 - M . l1

calculoLinha :: (Integral a, Num a ) => [[a]] -> Int -> [a]
calculoLinha c num =
    [ x - m * y | x <- c !! num]
    where m = 2 ;
                y  = c !! (num - 1) !! 2
