#간단한 압축풀기
T = int(input())
for i in range(1,T+1):
    num = int(input())
    arr=[]
    for j in range(num):
        ci,iter = input().split()
        for k in range(int(iter)):
            arr.append(ci)
    print("#{}".format(i))
    while(len(arr)>10):
        for j in range(10):
            print(arr[j],end="")
        print()
        arr[0:10] = []
    for j in range(len(arr)):
        print(arr[j],end="")
    print()
#####################################아래는 다른사람거 본것
# T = int(input())
# for i in range(1,T+1):
#     num = int(input())
#     ex=[]
#     for j in range(num):
#         ex.append(input().split(' '))
#     string = ''
#     for j in range(len(ex)):
#         string = string+ex[j][0]*int(ex[j][1])
#     count = 0
#     while(count<len(string)):
#         print(string[count],end="")
#         count = count+1
#         if(count%10==0):
#             print()
#         if(count==len(string)):
#             print()