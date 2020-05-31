#HASH
#전화번호부
phone_book = ["99","456", "97674223", "1195524421","12345","123456"]
answer = False
hash_map = dict()
for i in phone_book:
    hash_map[i] = 1
print(hash_map)
for i in phone_book:
    temp = ''
    for j in i:
        temp = temp +j
        if(temp in hash_map and temp != i):
            answer = False

print(answer)