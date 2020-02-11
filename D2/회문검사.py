T = int(input())
for i in range(1,T+1):
    string = input()
    flag=1
    length = len(string)
    mid = length//2
    if(length%2==0):
        mid+1
    for j in range(mid):
        if(string[j]!=string[length-1-j]):
            flag = 0
            break
    print("#{} {}".format(i,flag))