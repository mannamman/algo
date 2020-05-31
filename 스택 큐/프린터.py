#STACK_QUEUE : PRINTER
# 100%
priorities = [2,1,3,2]
location = 2
answer = 1
def check(priorities):
    cur = priorities.pop(0)
    for i in priorities:
        if(cur<i):
            priorities.append(cur)
            return True
    return False
    
while(priorities):
    flag = check(priorities)
    print("arr {}, location {},flag {}, answer {}".format(priorities,location,flag,answer))
    if(flag == True):
        if(location ==0):
            location = len(priorities) -1
        else:
            location = location -1
    else:
        if(location ==0):
            break
        else:
            answer = answer +1
            location = location-1

print(answer)
    
        