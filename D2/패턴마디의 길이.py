T = int(input())
for i in range(1,T+1):
    string = input()
    sum_str = ''
    for j in string:
        sum_str = sum_str+j
        length = len(sum_str)
        comp = string[length:length*2]
        print(sum_str,comp)
        if(sum_str==comp):
            break
    print("#{} {}".format(i,length))