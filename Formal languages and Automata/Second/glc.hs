import Data.Char
import Data.List

-- Parameters
sRt = getAsList "S"
glc = "aSb"
-- Parameters

data Tree = Tree {  root :: Node   , leng :: Int    } deriving (Show)
data Node = Node {  name :: String , next :: [Node] , isRoot :: Bool } deriving (Show)
                  
getLeng (Tree {leng = len}) = len
getRoot (Tree {root = rot}) = rot

getName (Node {name = nme}) = nme 
getNext (Node {next = nxt}) = nxt

getAsList :: String -> [String]
getAsList x = map(\xi -> [xi]) x

newTree :: Node -> Int -> Tree
newTree rot len = 
    Tree { root = rot, leng = len}

newNode :: String -> Bool -> Node
newNode name root = 
    Node { name = name, next = [], isRoot = root}

initialNod = newNode (sRt !! 0) True
otherNodes = map(\name -> newNode name False) (getAsList glc)

