#HEAP
#디스크 컨트롤러
#테스트케이스20성공
import heapq
jobs = [[0, 3], [1, 9], [2, 6]]
heap = list()
cnt = len(jobs)
answer = 0
before = -1
for i in range(cnt):
    heapq.heappush(heap,(sum(jobs[i]),i))
print(heap)
length = 0
while(cnt>0):
    temp = heapq.heappop(heap)
    index = temp[1]
    if(before == -1):
        answer = sum(jobs[index])
        before = index
        length = answer
        cnt = cnt - 1
    else:
        answer = answer + sum(jobs[index])-abs(jobs[before][1]-jobs[index][0]) + length
        length = jobs[index][1]
        cnt = cnt - 1
answer = answer / len(jobs)
print(answer)
        
    