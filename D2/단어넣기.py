##단어 넣기
T = int(input())
for i in range(1,T+1):
    N,M = map(int, input().split())
    key = '1'*M
    nums = []
    count = 0
    ##실제 실행부
    for j in range(N):
        num = input().split()
        num = list(num)
        nums.append(num)
    for j in range(N):
        temp=''
        for k in range(N):
            temp = temp+nums[j][k]
            if(nums[j][k]=='0'):
                temp=''
            if(temp==key):
                if(k==N-1):
                    count+=1
                    
                elif(nums[j][k+1]=='0'):
                    count+=1
                    
        temp = ''
        for k in range(N):
            temp+=nums[k][j]
            if(nums[k][j]=='0'):
                temp=''
            if(temp==key):
                if(k==N-1):
                    count+=1
                    
                elif(nums[k+1][j]=='0'):
                    count+=1
                    
    print("#{} {}".format(i,count))