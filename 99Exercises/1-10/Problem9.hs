{-
  Pack consecutive duplicates of list elements into sublists.
  If a list contains repeated elements they should be placed in separate sublists.
-}

import Data.List

pack xss =
    more xss ++ [concat (minus xss)]

more  xs =
    filter p (group xs)
            where p x = (length x) >= 2

minus xs =
    filter p (group xs)
            where p x = (length x) < 2
