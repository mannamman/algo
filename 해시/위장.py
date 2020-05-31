#HASH
#위장

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
#clothes = [["d","face"],["c","face"],["d","face"]]
answer = 0
temp = 1
hash_map = dict()
for i in clothes:
    if i[1] not in hash_map:
        hash_map[i[1]] = 1
    else:
        hash_map[i[1]] = hash_map[i[1]] +1
print(hash_map)
nums = list()
for i in hash_map:
    nums.append(hash_map[i]+1)
print(nums)
#(A종류 옷 가지수 + 1)*(B종류 옷 가지수 + 1)*(C종류 옷 가지수 + 1) - 1
#마지막의 -1은 아무것도 선택하지 않은 경우는 없어야하므로 제외 해준 것입니다.
for i in nums:
    temp = i*temp
answer = temp-1
print(answer)