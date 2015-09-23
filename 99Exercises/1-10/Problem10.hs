{-
- encode "aaaabccaadeeee"
- [(4,'a'),(1,'b'),(2,'c'),(2,'a'),(1,'d'),(4,'e')]
-
-}

import Data.List

data ListItem a = Single a | Multiple Int a deriving (Show)

p x = 
   map(\y -> (s (length y) y)) (group x)
--   map(\y -> (length y, y)) (group x)

s 1 x = (Single x)
s n x = Multiple n x

main = do
  name <- getLine
  print(p name)
  --print(map(\x -> (length x, x)) (group name))
