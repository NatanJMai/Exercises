{- 

-}

f :: (Fractional a, Floating a) => a -> a
f x =
	--exp(x) - tan(x)
	(2 * x) - 10

f' :: (Fractional a, Floating a) => a -> a
f' x =
	--exp(x) - (1 / cos² x)
	2

f'' :: (Fractional a, Floating a) => a -> a
f'' x =
	--exp(x) - 2 * (sin(x) / ((cos² x) * cos(x)))
	0
--cos² :: (Fractional a, Floating a) => a -> a
--cos² x = 
	--(1 + cos(2 * x)) / 2


func :: (Num x, Ord x, Fractional x, Floating x) =>x -> x -> x
func a e 
	| f(xn)      		== 0         = xn
	| abs(xx - xn)	<= e		= xx
	| otherwise					= func xx e
	where	xn					=  a;
			xx					= xn - (f xn / f' xn)
	
				
