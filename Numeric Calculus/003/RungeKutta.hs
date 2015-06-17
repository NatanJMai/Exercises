-- Parametros
b = 3
a = 1
n = (b - a) / h
h = 0.25

-- Definicoes
c  = round(n - 1) :: Int
x  = [a + (i * h) | i <- [0..n]]
y1 = [1]

-- Resultados
y'   = map (f') x
y    = ff y1 0
erro = zipWith (\ x y -> abs( x - y )) y y'

-- Impressao
main = do
  let zer = map (show) x
  let one = map (show) y
  let two = map (show) y'
  let thr = map (show) erro
  let fou = show h : ["<- h"]   ++ ["\n--------X---------"] ++ zer ++ ["\n---------Y--------"]
                                ++ one ++ ["\n---------Y'-------"]
                                ++ two ++  ["\n---------E--------"]
                                ++ thr
  let fiv = unlines fou
  putStrLn (fiv)


k1' x y i =
  h * f (elemE x i) (elemE y i)

k2' x y i =
  h * (f (elemE x i + (h * 0.5)) (elemE y i + (0.5 * k1' x y i)))

k3' x y i =
  h * (f (elemE x i + (h * 0.5)) (elemE y i + (0.5 * k2' x y i)))

k4' x y i =
  h * (f ((elemE x i) + h) ((elemE y i) + k3' x y i))

f x y  = (y / x) - ((y / x) ^ 2)
f' x   = x / (1 + log (x))

elemE xs n = xs !! n

calcK i yy =
  (elemE yy i) + (1/6) * (a +(2 * b) + (2 * c) + d)
     where a = k1' x yy i
           b = k2' x yy i
           c = k3' x yy i
           d = k4' x yy i

ff yy i
  | i           > c   = yy
  | otherwise         = ff a (i + 1)
  where a             = yy ++ [calcK i yy]
