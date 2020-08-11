module Exo where

sum' n = if n = 1 then n else n + (sum' n - 1)