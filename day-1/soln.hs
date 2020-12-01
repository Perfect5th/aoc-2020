import Data.List

main = do
    rawInput <- readFile "input.txt"
    let input = [read i :: Int | i <- lines rawInput] in
        do
            print $ soln1 input
            print $ soln2 input

soln1 input = head [x * y | (x:ys) <- tails input, y <- ys, x + y == 2020]

soln2 input = head [x * y * z | (x:ys) <- tails input,
                           (y:zs) <- tails ys,
                           z <- zs,
                           x + y + z == 2020]