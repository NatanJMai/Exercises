{-
- encode "aaaabccaadeeee"
- [(4,'a'),(1,'b'),(2,'c'),(2,'a'),(1,'d'),(4,'e')]
-
-}

import Data.List

main = do
  name <- getLine
  print(map(\x -> (length x, x)) (group name))
