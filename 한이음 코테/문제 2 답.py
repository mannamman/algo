#2
#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다
##아아니 왜 함수쓰면 안되
class Solution:
#     def deter(x):
#         left = x[:len(x)//2]
#         right = x[len(x)//2:]
#         left_sum = 0
#         right_sum = 0
#         for i in left:
#             left_sum = left_sum + int(i)
#         for i in right:
#             right_sum = right_sum + int(i)
#         return left_sum==right_sum
        
    def solution(self, s):
        big = 0
        for i in range(2,len(s)+1,2):
            for j in range(0,len(s),1):
                if(i+j>len(s)):
                    continue
                x = s[0+j:i+j]
                left = x[:len(x)//2]
                right = x[len(x)//2:]
                left_sum = 0
                right_sum = 0
                for q in left:
                    left_sum = left_sum + int(q)
                for q in right:
                    right_sum = right_sum + int(q)
                flag = left_sum==right_sum
                if(flag and big<len(x)):
                    big = len(x)
        return big
t=Solution()
t.solution("74233285")