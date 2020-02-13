#두개의 숫자열
T = int(input())
for i in range(1,T+1):
    N,M  = map(int,input().split())
    short=list(map(int,input().split()))
    long=list(map(int,input().split()))
    M = -9999
    if(len(short)>len(long)):
        temp = long
        long = short
        short = temp
    diff = len(long)-len(short)
    for j in range(diff+1):
        sumofarr = 0
        for k in range(len(short)):
            sumofarr = sumofarr+short[k]*long[k+j]
        if(sumofarr>M):
            M = sumofarr
    print("#{} {}".format(i,M))
