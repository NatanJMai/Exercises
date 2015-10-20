mymap :: (a -> b) -> [a] -> [b]
mymap f [] = []
mymap f (x:xs) = 
  [f x] ++ mymap f xs

a = take 14 [-1..]

b = sum $ reverse [x * x ^ 2 | x <- a]

--c = take 10 [2..]
c = sum [x ^ 2 | x <- take 10 [2..]]

