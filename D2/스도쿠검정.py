##스도쿠 검정
T = int(input())
for i in range(1,T+1):
    nums=[]
    for j in range(9):
        num = input().split()
        num = list(map(int,num))
        nums.append(num)
    #가로세로
    flag = 1
    for j in range(9):
        arr=[]
        for k in range(9):
            arr.append(nums[j][k])
        arr.sort()
        arr = list(set(arr))
        if(len(arr)!=9):
            flag = 0
        arr=[]
        for k in range(9):
            arr.append(nums[k][j])
        arr.sort()
        arr = list(set(arr))
        if(len(arr)!=9):
            flag = 0
    #구역
    for x in range(0,9,3):
        arr=[]
        for j in range(3):
            for k in range(3):
                arr.append(nums[j][k])
        arr.sort()
        arr = list(set(arr))
        if(len(arr)!=9):
            flag = 0
    print("#{} {}".format(i,flag))