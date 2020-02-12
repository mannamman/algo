##조교의 성적처리
T = int(input())
grade = ['D0','C-','C0','C+','B-','B0','B+','A-','A0','A+']
for i in range(1,T+1):
    total_num,student_num = map(int, input().split())
    upper = total_num//10
    nums=[]
    for j in range(total_num):
        num = input().split()
        num = list(map(int,num))
        temp = num[0]*0.35 + num[1]*0.45 + num[2]*0.2
        if(student_num ==j+1):
            student_num = temp
        nums.append(temp)
    nums.sort()
    index = nums.index(student_num)//upper
    print("#{} {}".format(i,grade[index]))
    
        