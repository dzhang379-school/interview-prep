arr = [[1, 4, 2],
       [2, 6, 4],
       [5, 7, 4],
       [3, 10, 7],
       [8, 11, 2],
       [9, 12, 1]]

maxV = 0
for i in xrange(6):
    maxV = max(maxV, arr[i][2])
    for k in xrange(i):
        if arr[k][1] < arr[i][0]:
            maxV = max(maxV, arr[i][2] + arr[k][2])
        maxV = max(maxV, arr[k][2])
    arr[i][2] = maxV

print(maxV)
