##지그재그 더하기
T = int(input())
for i in range(1,T+1):
    num = int(input())
    result = 0
    for j in range(1,num+1):
        if(j%2==0):
            j = j*-1
        result = result +j
    print("#{} {}".format(i,result))