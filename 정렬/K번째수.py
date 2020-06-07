#SORT
#K번째수
import heapq
array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = list()
for i in commands:
    temp = array[i[0]-1:i[1]]
    heapq.heapify(temp)
    result = 0
    for j in range(i[2]):
        result = heapq.heappop(temp)
    answer.append(result)

