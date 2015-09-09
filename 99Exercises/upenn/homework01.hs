{-
- Double the value of every second digit beginning from the right.
- That is, the last digit is unchanged; the second-to-last digit is doubled;
- the third-to-last digit is unchanged; and so on. For example,
- [1,3,8,6] becomes [2,3,16,6]. -
-}

-- We need to first find the digits of a number
toDigit :: Integer -> [Integer]
toDigit x 
  | x   <= 0  = []
  | otherwise   = map (\i -> read [i] :: Integer) (show x) 

toDigitReverse :: Integer -> [Integer]
toDigitReverse x = 
    reverse (toDigit x)
