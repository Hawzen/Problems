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


-- Problem 7 Have to know date types
-- prob17 :: [[]]


-- Problem 8
prob8 :: (Eq a) => [a] -> [a]
prob8 xs = foldr (\x acc -> if (head acc) == x then acc else x:acc) [last xs] (init xs)


-- Problem 9
prob9 :: (Eq a) => [a] -> [[a]]
prob9 [] = [[]]
prob9 (y:ys) = reverse $ foldl (\acc@(hd:tl) x -> if head hd == x then (x:hd):tl else [x]:acc) [[y]] ys


-- Problem 10
prob10 :: (Eq a) => [a] -> [(Int, a)]
prob10 xss = map (\xs -> (length xs, head xs)) $ prob9 xss



