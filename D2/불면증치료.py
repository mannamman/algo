#불면증치료
T = int(input())
for i in range(1,T+1):
    num = input()
    int_num = int(num)
    arr = list()
    cnt=0
    while(len(arr)<10):
        cnt = cnt+1
        for j in num:
            if(j not in arr):
                arr.append(j)
        num = int_num*cnt
        num = str(num)
    print("#{} {}".format(i,(cnt-1)*int_num))
    
            