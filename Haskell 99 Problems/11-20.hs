import Data.Map (Map)
import qualified Data.Map as Map

-- Problems: https://wiki.haskell.org/99_questions/1_to_10


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


-- Problem 16
prob16 :: Int -> [a] -> [a]
prob16 m = 
            let condition i = (i `mod` m) == 0
                checkAndExecute = (\acc (i, x) -> if condition i then acc else x:acc)
            in reverse . foldl checkAndExecute [] . zip [1,2..]


-- Problem 17
prob17 :: Int -> [a] -> ([a], [a])
prob17 m = 
        let sndAppend x acc = (fst acc, x:(snd acc))
            fstAppend x acc= (x:(fst acc), snd acc)
            checkAndAppend = (\acc (i, x) -> if m<i then sndAppend x acc else fstAppend x acc)
            rev acc = (reverse (fst acc), reverse (snd acc))
        in rev . foldl checkAndAppend ([], []) . zip [1,2..]

        
prob18 :: [a] -> Int -> Int -> [a]
prob18 xs i j = 
        let condition (_, m) = i <= m && m <= j
        in map fst $ ( filter condition (zip xs [1..]))


prob19 :: [a] -> Int -> [a]
prob19 xs i =
        let len = length xs
            condition i n = mod (n+(-i)) len
            keys = map (condition i)  [0..len-1]
            dict = Map.fromList $ zip keys xs
        in [dict Map.! key | key <- [0..len-1]]


prob20 :: Int -> [a] -> (a, [a])
prob20 m xs
        | length xs <= m = error "Ya broke it! list too small"
        | m <= 0 = error "Ya broke it! bad index"
        | otherwise =
            let list = (zip [1..] xs)
                acc = (xs !! (m-1), [])
                removeM = (\(i, x) acc -> if i==m-1 then acc else (fst acc, x:snd acc))
            in (foldr removeM acc list)

