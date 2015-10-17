fx :: (Num t, Eq t, Enum t) => t -> [(t, t)]
fx z = 
  take 1 [(x, y) | x <- [0..10], 
        	   y <- [0..10], 
       		   x + y == z]


ex2 = take 3 [1..]

ex3 :: (Num a) => (a -> a) -> a -> a
ex3 f x = 
    f x 


