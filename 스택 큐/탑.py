#STACK_QUEUE : TOWER
# 100%
heights = [6,9,5,7,4]
answer = []
for i in range(len(heights)):
    cur = heights[i]
    index = -1
    for j in range(i):
        if(cur<heights[j]):
            index = j
    answer.append(index+1)