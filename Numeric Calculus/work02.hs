import Data.List

-- Ajuste Multilinear
-- Xt * X * B = Xt * Y

a = [
  [-5, -4.75.. 5], 
  [x ^ 2 | x <- a !! 0], 
  [x ^ 3 | x <- a !! 0], 
  [x ^ 4 | x <- a !! 0],
  [x ^ 5 | x <- a !! 0]]
  -- [[-1, 0 , 1, 2, 4, 5, 5, 6],
  --  [-2, -1, 0, 1, 1, 2, 3, 4]]


p  = 4

y  = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00012341, 0.000519576, 0.00193046, 0.00632973, 0.0183157, 0.0467707, 0.105399, 0.209611, 0.36788, 0.569783, 0.778801, 0.939413, 1.0, 0.939413, 0.778801, 0.569783, 0.36788, 0.209611, 0.105399, 0.0467707, 0.0183157, 0.00632973, 0.00193046, 0.000519576, 0.00012341, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

xT = [[1 | x <- [0..40]]] ++ a

x  = zipp(\x y z w h-> [x, y, z, w, h]) (xT !! 0) (xT !! 1) (xT !! 2) (xT !! 3) (xT !! 4)

zipp _ [] _ _ _ _ = []
zipp _ _ [] _ _ _ = []
zipp _ _ _ [] _ _ = []
zipp _ _ _ _ [] _ = []
zipp _ _ _ _ _ [] = []
zipp f (x:xs)(y:ys)(z:zs)(w:ws)(h:hs) =
  f x y z w h: zipp f xs ys zs ws hs


for l1 l2 lim =
  [fff l1 l2 lim vl | vl <- [0..lim]]


fff l1 l2 nn jj =
  [sum(zipWith(\n y -> n * y) (colN yy l1) (l2 !! jj)) | yy <- [0..nn]]

colN n matrix =
  transpose matrix !! n


xTx = for x xT p
xTy = [(for x y  p) !! 0]

final = xTx ++ xTy
