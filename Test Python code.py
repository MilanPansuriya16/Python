matrix = [[1,2,3],[4,5,6],[7,8, 9]]

n = len(matrix)
m = len(matrix[0])

for i in range(n):
    for j in range(m):
        if i < j:
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

for i in range(n):
    for j in range(m):
        if j < m // 2:
            matrix[i][j],matrix[i][m-j-1] = matrix[i][m-j-1],matrix[i][j]


print(matrix)