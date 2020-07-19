def countStudents(height):
    # Write your code here
    Cur = 0
    Next = 0
    answer = 0
    for i in range(len(height)-1,0,-1):
        Cur = height[i]
        Next = height[i-1]
        if(Cur<=Next):
            answer = answer + 1
        if(i==len(height)-2 and Cur>=height[i+1]):
            answer = answer + 1
    return answer
