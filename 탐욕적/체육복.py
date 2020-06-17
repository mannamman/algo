#greedy
#체육복
n = 5
lost = [1,2,3,4,5]	
reserve = [1,2,3,4,5]	
temp = list()
answer = n-len(lost)
for i in lost
    if(i in reserve)
        reserve.remove(i)
        temp.append(i)
        answer = answer + 1
for i in temp
    if(i in lost)
        lost.remove(i)
for i in reserve
    if(answer==n)
        break
    elif(i-1 in lost)
        answer  = answer + 1
        lost.remove(i-1)
    elif(i+1 in lost)
        answer = answer +1
        lost.remove(i+1)
print(answer)