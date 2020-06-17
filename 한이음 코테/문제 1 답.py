#1
scores = [1,13,8,6,7,9]
#scores = list(set(scores)) 이놈때문에 다틀렸네
scores.sort()
print(scores)
big = -1
k=0

if(len(scores)%2!=0):
    for i in range(len(scores)//2+1):
        if(i==0):
            temp = sum(scores)/len(scores)
        else:
            temp = sum(scores[i:-i])/len(scores[i:-i])
        if(big<temp):
            big = temp
            k=i
else:
    for i in range(len(scores)//2):
        if(i==0):
            temp = sum(scores)/len(scores)
        else:
            temp = sum(scores[i:-i])/len(scores[i:-i])
        if(big<temp):
            big = temp
            k=i
if(k!=0):
    answer = sum(scores[k:-k])/len(scores[k:-k])
else:
    answer = sum(scores)/len(scores)
print(answer)