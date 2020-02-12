#날짜 계산기
dic = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
T = int(input())
for i in range(1,T+1):
    nums = input().split()
    nums = list(map(int,nums))
    result = dic[nums[0]]-nums[1]+1
    if(nums[0]!=nums[2]):
        result = result+ nums[3]
    for j in range(nums[0]+1,nums[2],1):
        result = result+dic[j]
        
    print("#{} {}".format(i,result))