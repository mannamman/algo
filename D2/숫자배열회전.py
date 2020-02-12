#숫자배열회전
T = int(input())
for i in range(1,T+1):
    N = int(input())
    nums = []
    for j in range(N):
        num = input().split()
        num = list(map(int,num))
        nums.append(num)
    d90=[]
    d180=[]
    d270=[]
    for j in range(N):
        small_temp=[]
        for k in range(N):
            small_temp.append(nums[N-1-k][j])
        d90.append(small_temp)
    nums = d90
    for j in range(N):
        small_temp=[]
        for k in range(N):
            small_temp.append(nums[N-1-k][j])
        d180.append(small_temp)
    nums = d180
    for j in range(N):
        small_temp=[]
        for k in range(N):
            small_temp.append(nums[N-1-k][j])
        d270.append(small_temp)
    nums = d270
    print("#{}".format(i),end="")
    for j in range(N):
        print()
        for k in d90[j]:
            print(k,end="")
        print(" ",end="")
        for k in d180[j]:
            print(k,end="")
        print(" ",end="")
        for k in d270[j]:
            print(k,end="")
        print(" ",end="") 
    print()
                
            
    