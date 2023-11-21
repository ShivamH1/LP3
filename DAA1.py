def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

def non_recur_fibo(n):
    first = 0
    second = 1
    print(first)
    print(second)
    while n-2 > 0:
        third = first+second
        first = second
        second = third
        print(third)
        n -= 1

if __name__ == '__main__':
    n = 8
    for i in range(n):
        print(recur_fibo(i))
    
    non_recur_fibo(n)