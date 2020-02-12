##쉬운 거스름돈
T = int(input())
money = [50000,10000,5000,1000,500,100,50,10]
for i in range(1,T+1):
    num = int(input())
    arr=[]
    for j in money:
        val = num//j
        if(val!=0):
            num = num-j*val
        arr.append(val)
    print("#{}".format(i))
    for j in arr:
        print(j,end=" ")
    print()