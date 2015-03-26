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


--calcM :: (Num a , Fractional a, Integral a) =>a -> a -> a
calcM a b =
    a / b

-- l2 = l2 - M . l1

{- f :: (Num a, Fractional a)=> a -> a -> a
f x y = do
    let m = calcM 4 2
    x - m * y -}

--calculo :: (Num a, Fractional a, Integral a) => [a] -> [a] -> [a]
calculo xs ys ind= do
    zipWith ( \x y -> y - m * x ) xs ys
        where m = calcM (ys !! ind) (xs !! ind)

--gauss :: (Num a, Fractional a, Integral a) => [[a]] -> [a]
gauss xs piv k =
    [[x | x <- xs !! a]] ++  [[y |y <- calculo (xs !! a)(xs !! (a + 1)) 0 ]]  ++  [[z | z <-  calculo(xs !! a)(xs !! (a + 2)) 0]]
      where a = k - 1


 --[ | x <- xs !! 0, y <- calculo (xs !! 0)(xs !! 1), z <-  calculo(xs !! 0)(xs !! 2)]
 --xs !! 0 ++ calculo (xs !! 0)(xs !! 1) ++  calculo(xs !! 0)(xs !! 2)
gauss' xs piv k =
    [[x | x <- xs !! a]] ++  [[y |y <- calculo (xs !! a)(xs !! (a + 1)) 1 ]]
        where a = k - 1
