module Util(
  elemn      , 
  verifyElem , 
) where 

import Data.List

elemn xs =
    [ y | y <- xs, verifyElem y xs == True]



verifyElem b xs =
    if b `elem` xs \\ [b] then 
        False
    else
        True

