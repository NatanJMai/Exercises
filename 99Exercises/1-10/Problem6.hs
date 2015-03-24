{-
    Find out whether a list is a palindrome. A palindrome can be read forward or backward; e.g. (x a m a x).
-}

palind :: (Eq a) => [a] -> Bool
palind xs
    | reverse xs    == xs        = True
    | otherwise                       = False
