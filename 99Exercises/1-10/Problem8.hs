{-
    Eliminate duplicates of list elements.
-}

import Data.List

elemn xs =
    [ y | y <- xs, verifyElem y xs == True]


verifyElem b xs =
    if b `elem` deleteElem b xs then
        False
    else
        True

deleteElem b xs =
    delete b xs
