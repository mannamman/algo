#RC카
T = int(input())
for i in range(1,T+1):
    num = int(input())
    ac = 0
    dis = 0
    for j in range(num):
        try:
            com,val = map(int, input().split())
        except ValueError:
            com=0
        if(com==1):
            ac = ac+val
        elif(com==2):
            ac = ac-val
            if(ac<0):
                ac = 0
        dis = dis+ac
    print("#{} {}".format(i,dis))
            