def spiralMatrix(a):
    rowLength = len(a[0])
    colLength = len(a)

    numLayers = min( rowLength // 2, colLength // 2)

    for i in range(numLayers + 1):
        for x in a[i][i:rowLength - i]:
            print(x)
        for x in (a[j][rowLength - i - 1] for j in range(i + 1, colLength - i)):
            print(x)
        for x in a[colLength - i - 1][rowLength - i - 2:i:-1]:
            print(x)
        for x in (a[j][i] for j in range(colLength - i - 1, i, -1)):
            print(x)

A = [[1, 2, 3, 4],
     [8, 2, 5, 1],
     [3, 10, 7, 9]]

spiralMatrix(A)