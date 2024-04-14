def countdown(n):
    print(n)
    if n == 0:
        print("readed base case")
        return
    
    
    countdown(n - 1)
    print(n)

countdown(3)