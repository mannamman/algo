#HEAP
#더 맵게
import heapq
scoville = [1, 2, 3, 9, 10, 12]	
K = 9999
answer = 0
heapq.heapify(scoville)

while(scoville[0]<K):
    try:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville,first+second*2)
        answer = answer + 1
    except:
        answer = -1
print(answer)
