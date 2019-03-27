def getSeed(n):

    for i in range(n):
        digits = str(i)
        k = i
        for x in digits:
            k *= int(x)
        if k == n:
            print(i)

A = [1, 2, 3, 4, 5, 6, 7]

print(A[3::-1])