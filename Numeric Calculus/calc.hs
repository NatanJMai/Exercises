func1 = 
    [[a,b,c,d] |  
                    a <- [-10..10], 
                    b <- [-10..10], 
                    c <- [-10..10], 
                    d <- [-10..10], 
                    ((3 * a) + (4 * b) - (5 * c) + d)   == (-10), 
                                         (b + c) - (2 * d )   == -1, 
                                         (4  * c) - (5 * d )   == 3,
                                                       (2 * d )   == 2]


divideByTen :: (Floating a) => a -> a
divideByTen = (/10)

teste :: (Num a) => [a] -> [a]
teste (x:xs) = xs