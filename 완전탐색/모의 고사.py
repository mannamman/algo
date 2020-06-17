#BP
#모의 고사
import operator
answers = [1,3,2,4,2]
length = len(answers)
student1 =  [1, 2, 3, 4, 5]
student2 = [2, 1, 2, 3, 2, 4, 2, 5]
student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
while(len(student1)<=length):
    student1 = student1*2
while(len(student2)<=length):
    student2 = student2*2
while(len(student3)<=length):
    student3 = student3*2
h = {
    "1" : 0,
    "2" : 0,
    "3" : 0
}
for a,s1,s2,s3 in zip(answers,student1,student2,student3):
    if(a==s1):
        h["1"] = h["1"] + 1
    if(a==s2):
        h["2"] = h["2"] + 1
    if(a==s3):
        h["3"] = h["3"] + 1
h = sorted(h.items(),key = operator.itemgetter(1),reverse=True)
print(h)
h = [list(i) for i in h]
big = h[0][1]
for i in range(len(h)):
    if(h[i][1]<big):
        h[i][1]=0
answer = [int(i[0]) for i in h if i[1]!=0]
print(answer)