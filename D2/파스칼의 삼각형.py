T = int(input())
for i in range(1,T+1):
    n = int(input())
    small=[1]
    big=[]
    print("#{}".format(i))
    for j in range(n):
        for k in range(j+1):
            left,right = k-1,k
            if(left<0 or right==len(small)):
                big.append(1)
                print(1,end=" ")
            else:
                sum = small[left]+small[right]
                big.append(sum)
                print(sum,end=" ")
        small=big
        big=[]
        print()