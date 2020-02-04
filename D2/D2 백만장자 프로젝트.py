T = int(input())
for i in range(1,T+1):
    N = int(input())
    arr=input()
    arr = arr.split()
    arr=[int(x) for x in arr]
    max = arr[N-1]
    sum = 0
    for j in range(N-2,-1,-1):
        if(max<arr[j]):
            max = arr[j]
        else:
            sum = sum+max-arr[j]
    print("#{} {}".format(T,sum))