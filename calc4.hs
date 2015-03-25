import Data.List
import Data.Maybe (fromJust)

{-
    Gauss Method
-}

teste :: Int
teste = 2

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
calculo xs ys = do
    zipWith ( \x y -> y - m * x ) xs ys
        where m = calcM (ys !! 0) (xs !! 0)

--gauss :: (Num a, Fractional a, Integral a) => [[a]] -> [a]
gauss xs = do
    [[x | x <- xs !! 0]] ++ [[y |y <- calculo (xs !! 0)(xs !! 1)]] ++ [[z | z <-  calculo(xs !! 0)(xs !! 2)]]

    --[ | x <- xs !! 0, y <- calculo (xs !! 0)(xs !! 1), z <-  calculo(xs !! 0)(xs !! 2)]
    --xs !! 0 ++ calculo (xs !! 0)(xs !! 1) ++  calculo(xs !! 0)(xs !! 2)
