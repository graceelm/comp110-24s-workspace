def f(n: int, b: int) -> int:
    if n == 0: # base case
        return b
    else: # recursive rule
        return 1 + f(n-1, b)
    
print(f(3,4))