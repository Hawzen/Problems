-- Problems: https://wiki.haskell.org/99_questions/1_to_10

-- Problem 1
prob1 :: [a] -> a
prob1 [] = error "Empty list"
prob1 xs = last xs

-- Problem 2
prob2 :: [a] -> a
prob2 [] = error "Empty list"
prob2 xs
    | length xs == 1 = head xs
    | otherwise = let x = init xs in last x

-- Problem 3
prob3 :: [a] -> Int -> a
prob3 [] i = error "Empty list"
prob3 xs i = case len of True -> xs !! (i - 1)
                         False -> error "Index out of range"
    where len = length xs >= i

-- Problem 5
prob5 :: [a] -> [a]
prob5 [] = []
prob5 xs = [last xs] ++ prob5 (init xs)

-- Problem 6
prob6 :: (Eq a) => [a] -> Bool
prob6 xs = xs == prob5 xs

{- 
Problem 7
(**) Flatten a nested list structure.

Transform a list, possibly holding lists as elements into a `flat' list by replacing each list with its elements (recursively).

Example:

* (my-flatten '(a (b (c d) e)))
(A B C D E)
Example in Haskell:

We have to define a new data type, because lists in Haskell are homogeneous.

 data NestedList a = Elem a | List [NestedList a]
λ> flatten (Elem 5)
[5]
λ> flatten (List [Elem 1, List [Elem 2, List [Elem 3, Elem 4], Elem 5]])
[1,2,3,4,5]
λ> flatten (List [])
[]
-}

-- Problem 9
prob9 :: (Eq a) => [a] -> [[a]]
prob9 [] = [[]]
prob9 (y:ys) = reverse $ foldl (\acc@(hd:tl) x -> if head hd == x then (x:hd):tl else [x]:acc) [[y]] ys


-- Problem 10
prob10 :: (Eq a) => [a] -> [(Int, a)]
prob10 xss = map (\xs -> (length xs, head xs)) $ prob9 xss



