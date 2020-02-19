#최빈수 구하기
dic={}
for i in range(101):
    dic[i]=0
T = int(input())
for i in range(1,T+1):
    num = int(input())
    nums = list(map(int,input().split()))
    keys=[]
    for j in nums:
        dic[j] = dic[j]+1
    M = -9999999
    for j in dic:
        if(dic[j]>=M):
            M = dic[j]
            keys.append(j)
    print(keys)
    print("#{} {}".format(i,keys[len(keys)-1]))