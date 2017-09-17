lim = int(raw_input())


def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
i = 2
for i in range(i, lim):
    if fibo(i) > lim and fibo(i-1) > lim:
        break
    for e in range(fibo(i-1)+1, fibo(i)):
        if e < lim:
            print e,
        else:
            break
