#SORT
#H-index
#문제 지문이 좀
#맞는거같은데...
#citations = [3, 0, 6, 1, 5]
#citations = [0,1,1,1,1,3,3,4]
#citations = [5,5,5,5,5]
citations = [1,23,4,6,5,234,6,46,2]
citations.sort(reverse=True)#65310
answer = 0
for i in citations:
    bcnt = 0
    scnt = 0
    for j in citations:
        if(i<=j):
            bcnt = bcnt +1
        else:
            scnt = scnt + 1
    print(i,bcnt,scnt)
    if(bcnt>=i and scnt<=i and scnt != 0):
        answer = i
        break
print(answer)