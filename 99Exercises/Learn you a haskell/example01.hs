{-
    PhoneBook
-}

import Data.Map

phoneBook = [("Natan", 123), ("Teste", 456)]

findKey :: (Eq a) => a -> [(a, v)] -> Maybe v
findKey key [] =  Nothing
findKey key ((kk, vv):xs) =
    if kk == key then
        Just vv
    else
        findKey key xs


cuboidVolume :: Float -> Float
cuboidVolume = (/ 10)


