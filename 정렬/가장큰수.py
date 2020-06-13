#SORT
#가장큰수
#풀이를 봤음
numbers = [6,100,2]
numbers = [str(i) for i in numbers]
numbers.sort(key = lambda a : a*4,reverse=True)
answer = str(int(''.join(numbers))) #int형변환 하는것은 0000같은것을 0으로 줄여줌
print(answer)