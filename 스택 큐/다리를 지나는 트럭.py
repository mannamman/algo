#STACK_QUEUE : CROSS THE BRIGE
#100% 통과 실패 42.9의 정확성, 시간초과와 테스트케이스 실패 이유는 모르겠어

bridge_length = 100
weight = 100
truck_weights = [1,2]
bridge = [0] * bridge_length
answer = 0
index = 0
def move(bridge):
    for i in range(len(bridge)):
        if(i==len(bridge)-1):
            continue
        bridge[i] = bridge[i+1]

while(index<len(truck_weights)+1):
    print(bridge)
    if(index<len(truck_weights)):
        if(sum(bridge)+truck_weights[index]<=weight):
            move(bridge)
            bridge[-1] = truck_weights[index]
            answer = answer +1
            index = index+1
        elif(sum(bridge)+truck_weights[index]-bridge[0]<=weight):
            bridge[0] = 0
            bridge[-1] = truck_weights[index]
            index = index+1
            answer = answer +1
        else:
            move(bridge)
            bridge[-1] = 0
            answer = answer + 1
    else:
        if(sum(bridge)==0):
            break
        move(bridge)
        bridge[-1] = 0
        answer = answer+1
print(answer)
