#다트게임
dartResult = "1D2S#10S"
arr = list(dartResult)
arr.reverse()
temp = list()
answer = 0
string = ''
flag = True
for i in arr:
    if(ord(i)>=48 and ord(i)<=57):
        flag = True
    else:
        flag = False
    if(len(string)>1 and flag == False):
        temp.append(string)
        string = ''
    string = string + i
temp.append(string)
cnt = 0
for i in temp:
    event = 1
    square = 1
    nums = ''
    for j in i:
        char = ord(j)
        if(char==42 or char==35):
            event = j
        elif(char==83 or char==84 or char ==68):
            square = j
        else:
            nums = nums + j
    nums = sorted(nums,reverse=True)
    nums = ''.join(nums)
    nums = int(nums)
    if(square == 'T'):
        square = 3
    elif(square=='D'):
        square = 2
    elif(square =='S'):
        square = 1
    if(event =='*'):
        event = 2
        cnt = cnt +2
    elif(event =='#'):
        event = -1
    if(cnt == 2):
        answer = answer + 2*(nums**square)
        cnt = cnt -1
    elif(cnt>0):
        answer = answer + 2*event*(nums**square)
        cnt = cnt -1
    else:
        answer = answer + event*(nums**square)
print(answer)