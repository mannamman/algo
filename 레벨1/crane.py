def solution(board, moves):
    cnt = 0
    arr = []
    answer = 0
    for i in board:
        if(sum(i)==0):
            cnt = cnt + 1
        else:
            break
    for i in range(cnt):
        board.pop(0)
    for i in moves:
        default = 0
        for j in range(len(board)):
            print(board[j][i-1],i-1,j)
            if(board[j][i-1]!=0):
                default = board[j][i-1]
                board[j][i-1] = 0
                arr.append(default)
                break
        if(len(arr)>=2 and arr[-1]==arr[-2]):
            answer = answer + 2
            arr.pop()
            arr.pop()
    return answer
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))