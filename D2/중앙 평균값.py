##중앙 평균값
T = int(input())
for i in range(1,T+1):
    nums = input().split()
    nums = list(map(int,nums))##좋은거같은데
    Min,Max = 99999,-99999
    result = 0
    for j in nums:
        if(j>Max):
            Max = j
        if(j<Min):
            Min = j
        result = result+j
    result = round((result-Min-Max)/8,1)
    print("#{} {}".format(i,result))