insert :: Int -> [Int] -> [Int]
insert vect a = 
   [vect] ++ a

a = foldr insert [] [2,3]
