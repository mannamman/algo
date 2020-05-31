#STACK_QUEUE : PRICE
#역으로 가면서
#prices = [1, 2, 3, 2, 3]
prices = [5,2,1,2,1]
answer = list()
answer.append(0)
for i in range(len(prices)-2,-1,-1):
    count = 0
    for j in range(i,len(prices)):
        if(prices[i]>prices[j]):
            count = count +1
    answer.append(len(prices)-i-1-count)
answer.reverse()
print(answer)

    
