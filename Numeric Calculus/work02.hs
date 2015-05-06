import Data.List

-- Ajuste Multilinear
-- Xt * X * B = Xt * Y

n = 8
a = [[-1, 0 , 1, 2, 4, 5, 5, 6],
     [-2, -1, 0, 1, 1, 2, 3, 4]]

y = [[13, 11, 9, 4, 11, 9, 1, -1]]

xT = [[1, 1, 1, 1, 1, 1, 1, 1]] ++ a

x  = zipWith3(\x y z -> [x, y, z]) (xT !! 0) (xT !! 1) (xT !! 2)


for l1 l2 lim =
    [fff l1 l2 lim vl | vl <- [0..lim]]


fff l1 l2 nn jj =
    [sum(zipWith(\n y -> n * y) (colN yy l1) (l2 !! jj)) | yy <- [0..nn]]

colN n matrix =
    transpose matrix !! n


xTx = for x xT 2
xTy = [(for x y  2) !! 0]


final = xTx ++ xTy

