{-
    Implementation of a numerical method for find the roots. 
    Receive one function defined, two points (a, b) and
    a list with the values between a and b.

    Example: 
        f(x) = (2 * x) - 10
        > function 4 6 
            result = 5.0 (OK)

        > function 4 7
            result = 5.0 (OK)
-}

a = (-1.0)
b = 2.0

list = 
    [a, (-0.5) .. b]

-- Função em torno de x.
fx :: (Num a) => a -> a
fx x = (2 * x) - 10

f :: (Ord a, Num a) => a -> a -> a
f x y =
    fx x * fx y

function :: (Num a, Fractional a, Ord a) => a -> a -> a
function a b  
    | fx x1                 <= (-1.0)     = x1 
    | fx x1                  == 0          = x1
    | fx a * fx x1         == 0           = x1
    | fx a * fx x1           > 0            = function x1 b
    | fx a * fx x1           < 0            = function a x1
    | fx b * fx x1           > 0            = function a x1
    | fx b * fx x1           < 0            = function x1 b
    where                      x1             = (a + b) / 2