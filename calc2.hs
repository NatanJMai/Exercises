{-
	Implementation of a numerical method for find the roots. 
	Receive one function defined, two points (a, b) and
	a list with the values between a and b.

	Example: 
	f(x) = (2 * x) + 8
    		> function (-4) 6 
			result = -4.0 (OK)	
-}

{-      Other method        -}

fx :: (Num a, Ord a) => a -> a
fx x  
	| c < 0			= (- c)
	| otherwise		= c
	where          c	= (2 * x) + 8

getX :: (Num a, Fractional a, Ord a) => a -> a -> a
getX a b = 
	((a * fx b) + (b * fx a)) / (fx a + fx b)

function :: (Num a, Fractional a, Ord a) => a -> a -> a
function a b  
	| fx a                 == 0	= a
	| fx b                 == 0	= b
	| fx x1               <= 0	= x1 
	| fx x1               == 0	= x1
	| fx a * fx x1      == 0	= x1
	| fx a * fx x1      > 0   	= function x1 b
	| fx a * fx x1      < 0   	= function a x1
	| fx b * fx x1      > 0   	= function a x1
	| fx b * fx x1      < 0   	= function x1 b
	where                 x1   	= getX a b
