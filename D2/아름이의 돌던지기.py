#아름이의 돌던지기
T = int(input())
for i in range(1,T+1):
    nums = int(input())
    arr = list(map(int,input().split()))
    for j in range(len(arr)):
        if(arr[j]<0):
            arr[j]*=-1
    arr.sort()
    cnt=1
    for j in range(1,len(arr)):
        if(arr[0]!=arr[j]):
            break
        cnt+=1
    print("#{} {} {}".format(i,arr[0],cnt))