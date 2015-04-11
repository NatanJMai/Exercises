calcM a b =
    a / b

calculo xs ys ind= do
    zipWith ( \x y -> y - m * x ) xs ys
        where m = calcM (ys !! ind) (xs !! ind)


fazCalculo xs = do
    let bb = pivos xs 0 0 0
    return (pivos bb 0 1 0)

--
pivos xs pivo indice jjj
    -- Isso para pivo 0
    | pivo              == 0    = att xs pivo (indice + 1) jjj ++ att xs pivo (indice + 2) jjj
    | pivo              == 1    = att xs pivo (indice + 1) (jjj + 1)


att xs pivo indice jjj =
    [[y |y <- calculo (xs !! pivo)(xs !! indice) jjj ]]
