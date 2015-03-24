{-
Find the last but one element of a list.
(Note that the Lisp transcription of this problem is incorrect.)
Example in Haskell:
    Prelude> myButLast [1,2,3,4]
        3
    Prelude> myButLast ['a'..'z']
        'y'
-}

lastButOne :: [a] -> a
lastButOne []   = error "Nope"
lastButOne [a] = error "Nope"
lastButOne xs  =
    xs !! (length xs  -  2)
