{-
    Eliminate consecutive duplicates of list elements.
-}

elemn :: (Eq a) => [a] -> [a]
elemn xs = do
    y <- xs
    return y
