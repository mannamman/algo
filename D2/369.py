N = int(input())
N = [i for i in range(1,N+1)]
for i in range(len(N)):
    count = 0
    for j in str(N[i]):
        if(j=='3' or j=='6' or j=='9'):
            count = count+1
        else:
            continue
    if(count>0):
        N[i] = '-'*count
    print(N[i],end=" ")