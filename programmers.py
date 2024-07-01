# str = input()
# print('\n'.join(str))

# 비트연산자 이용
# a = int(input())
# print(f'{a} is {'eovdedn'[a&1::2]}')

# 문자열 겹쳐쓰기
def solution(my_string, overwrite_string, s):
    answer = my_string[0:s] + overwrite_string + my_string[s + len(overwrite_string) : ] 
    return answer
print(solution("Hello12345678", "World", 5))

# 문자열 섞기
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    return answer
print(solution('aaa','bbb'))

# 문자 리스트를 문자열로 변환하기   -> join쓰면 한 줄로 작성 가능함
def solution(arr):
    answer = ''
    for i in range(len(arr)):
        answer += arr[i]
    return answer
print(solution(['a','b','c']))

def solution(arr):
    return ''.join(arr)
print(solution(['a','b','c']))

# lambda = def
solution = lambda l: ''.join(l)
print(solution(['a','b','c']))

# 문자열 곱하기
solution = lambda str,k: str*k
print(solution('abc',3))

# 더 크게 합치기
def solution(a, b):
    data1 = str(a) + str(b)
    data2 = str(b) + str(a)
    if int(data1) > int(data2):
        return int(data1)
    else:
        return int(data2)

# 두 수의 연산값 비교하기
solution = lambda a,b: max(int(str(a)+str(b)), 2*a*b)
print(solution(3,12))