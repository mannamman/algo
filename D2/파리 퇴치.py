T = int(input())
for i in range(1,T+1):
    n, m = map(int, input().split())
    N=[]
    for j in range(n):
        nums = input().split()
        for k in range(len(nums)):
            nums[k] = int(nums[k])
        N.append(nums)
    M = -99999
    for x in range(n-m+1):
        start,end=0,m
        for j in range(n-m+1):
            result = 0
            for k in range(x,x+m):
                result = sum(N[k][start+j:end+j])+result
            if(M<result):
                M=result
    print("#{} {}".format(i,M))