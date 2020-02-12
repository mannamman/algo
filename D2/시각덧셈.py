T  = int(input())
for i in range(1,T+1):
    nums = input().split()
    nums = list(map(int,nums))
    m = nums[1]+nums[3]
    if(m>=60):
        nums[0] = nums[0]+1
    m = m%60
    h = nums[0]+nums[2]
    if(h%12==0):
        h = 12
    else:
        h = h%12
    print("#{} {} {}".format(i,h,m))