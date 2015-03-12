{- 

-}

f :: (Fractional a, Floating a) => a -> a
f x =
	exp(x) - tan(x)

cos² :: (Fractional a, Floating a) => a -> a
cos² x = 
	(1 + cos(2 * x)) / 2

f' :: (Fractional a, Floating a) => a -> a
f' x =
	exp(x) - (1 / cos² x)