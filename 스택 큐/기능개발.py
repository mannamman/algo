#STACK_QUEUE : FUNCTION DEVELOP
# 100%

import math
progresses = [42,16,55,27,19,8,79,91]
speeds = [10,13,5,11,20,9,15,3]
answer = list()
deter = 0
index = -1
for i in range(len(progresses)):
    remain = math.ceil(((100-progresses[i])/speeds[i]))
    if(deter<remain):
        deter = remain
        answer.append(1)
        index = index + 1
    else:
        answer[index] = answer[index] + 1
print(answer)
        