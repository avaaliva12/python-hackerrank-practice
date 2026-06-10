def prime(n):
    p = 0
    for i in range(1, n+1):
        if n%i == 0:
            p += 1
    
    if p == 2:
        print(f"{n} is Prime Number")
    else:
        print(f"{n} is not a Prime Number")

prime(2)
prime(7)
prime(4)
prime(8)