##해쉬이용 배열에서 타겟넘버가 되는 두 수의 인덱스를 구하라
target = int(input("target : "))
nums = input().split()
#nums = [int(i) for i in nums]
nums = list(map(int,nums)
dic={}
for i in range(target):
    dic[i]=-1
for i in range(len(nums)):
    key = 0
    if(target>nums[i]):
        key = target-nums[i]
        dic[key] = i
    if(dic[target-key]!=-1):
        print("index1 {}, index2 {}".format(dic[target-key],dic[key]))
        break

    