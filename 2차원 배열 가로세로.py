temp = [[0, 0, 1, 1, 1], [1, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 1], [1, 1, 1, 0, 1]]
for i in range(5):
    for j in range(5):
        print("가로 : ",temp[i][j])
    for j in range(5):
        print("세로 : ",temp[j][i])