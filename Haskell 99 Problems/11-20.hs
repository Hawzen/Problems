-- Need to learn data types or something for 11 - 13

-- -- Problem 11
-- prob9 :: (Eq a) => [a] -> [[a]]
-- prob9 [] = [[]]
-- prob9 (y:ys) = reverse $ foldl (\acc@(hd:tl) x -> if head hd == x then (x:hd):tl else [x]:acc) [[y]] ys

-- prob11 :: (Eq a) => [a] -> [(Int, a), a]
-- prob11 = map (\xs -> if p xs then (length xs, head xs) else head xs) $ prob9 
--             where p = 1<  length

-- Problem 14
prob14 :: [a] -> [a]
prob14 = foldl1 (++) . map (\x -> [x,x])

-- Problem 15
prob15 :: (Enum a) => Int -> [a] -> [a]
prob15 i =  let replicate x = take i [x,x..] 
            in foldl (\acc x -> acc ++ replicate x) [] 

-- I am dizzy now, return later
-- -- Problem 16
-- prob16 :: Int -> [a] -> [[a]]
-- prob16 i =  let p acc = length acc < i
--             in foldl (\(hd:la) x -> if p hd then x:hd else x:head la) [[]]
-- -- prob16 i = takeWhile length 