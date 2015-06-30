import Data.Char
import Data.List
import Util

-- glc = "S-> [[aS], [SS], [bA], [$]]"
glc  = ["S -> bSb | aSS | bA | vx"]
glc2 = ["T -> bSb"]
n    = (length (glc !! 0)) - 1
x    = (length glc) - 1

data Node  = Node  {name :: String, next :: [Node]} deriving (Show)
data First = First {nam :: [Char] , conj :: [Node]} deriving (Show)

newNode :: String -> Node
newNode nam = 
    Node {name = nam, next = []}

newLowerFirst :: [Char] -> First
newLowerFirst nm = 
    First {nam = nm, conj = [getNode nm]}

getNode :: String -> Node
getNode nam = take 1 ([(initialNodes1 !! i) | i <- [0..], name (initialNodes1 !! i) == nam ]) !! 0 

getFirstConjLow :: String -> First
getFirstConjLow nm = take 1 ([(terminals !! i) | i <- [0..], nam (terminals !! i) == nm]) !! 0

getName (Node {name  = nm}) = nm 

getAsList :: [Char] -> [[Char]]
getAsList x = map(\xi -> [xi]) [x !! i | i <- [5..n]]

firstNode = [newNode [(glc !! xi) !! 0] | xi <- [0..x]]

--
-- ###########################
-- ###########################
--

listString = filter (/= " ") (getAsList (glc !! 0))
a          = nub ([getName (firstNode !! 0)] ++ (filter (/= "|") listString))

initialNodes1 = map (\ai -> newNode ai) a 
names         = [getName x | x <- initialNodes1]
namesChar     = filter (isLower) (unlines names)

-- Create the lower nodes, e.g: a, b and c.

terminals = [newLowerFirst [xi] | xi <- namesChar]

returnNext line = do
    let a = takeWhile (/= "|") listString
    let c = takeWhile (/= "|") (listString \\ (a ++ ["|"]))
    let d = takeWhile (/= "|") (listString \\ (a ++ ["|"] ++ c ++ ["|"]))
    let e = takeWhile (/= "|") (listString \\ (a ++ ["|"] ++ c ++ ["|"] ++ d ++ ["|"]))
    let frst = nub [(a !! 0), (c !! 0), (d !! 0), (e !! 0)] 

    let ca = nub [any isUpper ([frst] !! 0 !! x) | x <- [0..length([frst]!! 0) - 1]]
    
    if (ca !! 0) == False then 
      return ([frst], ca)
    else
      -- TODO -> First to UPPER
      return ([], ca)



searchFirst nme = do
    let a = getNode nme
    if name a == nme then 
      putStrLn(name a)
    else 
      putStrLn("Teste")
    







