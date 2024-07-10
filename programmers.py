# # str = input()
# # print('\n'.join(str))

# # 비트연산자 이용
# # a = int(input())
# # print(f'{a} is {'eovdedn'[a&1::2]}')

# # 문자열 겹쳐쓰기
# def solution(my_string, overwrite_string, s):
#     answer = my_string[0:s] + overwrite_string + my_string[s + len(overwrite_string) : ] 
#     return answer
# print(solution("Hello12345678", "World", 5))

# # 문자열 섞기
# def solution(str1, str2):
#     answer = ''
#     for i in range(len(str1)):
#         answer += str1[i] + str2[i]
#     return answer
# print(solution('aaa','bbb'))

# # 문자 리스트를 문자열로 변환하기   -> join쓰면 한 줄로 작성 가능함
# def solution(arr):
#     answer = ''
#     for i in range(len(arr)):
#         answer += arr[i]
#     return answer
# print(solution(['a','b','c']))

# def solution(arr):
#     return ''.join(arr)
# print(solution(['a','b','c']))

# # lambda = def
# solution = lambda l: ''.join(l)
# print(solution(['a','b','c']))

# # 문자열 곱하기
# solution = lambda str,k: str*k
# print(solution('abc',3))

# # 더 크게 합치기
# def solution(a, b):
#     data1 = str(a) + str(b)
#     data2 = str(b) + str(a)
#     if int(data1) > int(data2):
#         return int(data1)
#     else:
#         return int(data2)

# # 두 수의 연산값 비교하기
# solution = lambda a,b: max(int(str(a)+str(b)), 2*a*b)
# print(solution(3,12))

# # n의 배수

# def solution(num, n):
#     answer = 1 if  num % n == 0 else 0
#     return answer
# # 공배수

# def solution(number, n, m):
    
#     if (number % n == 0) and (number % m == 0):
#         return  1
#     else:
#         return  0
    
# # 홀짝에 따라 다른 값 반환하기
# def solution(n):
#     answer1 = 0
#     answer2 = 0
#     for i in range(n+1):
#         if i % 2 == 1:
#             answer1 += i
#         else:
#             answer2 += i*i
    
#     return answer1 if n % 2 == 1 else answer2


# # flag에 따라 다른 값 반환하기
# def solution(a, b, flag):
#     return a+b if flag == True else a-b

# # 원소들의 곱과 합
# def solution(num_list):
#     answer1 = 1
#     answer2 = 0
#     for i in range(len(num_list)):
#         answer1 *= num_list[i]
#         answer2 += num_list[i]
#     return 1 if answer1 < answer2**2 else 0
   
# #  조건 문자열

# def solution(ineq, eq, n, m):
#     if ineq == '>' and eq == '=':
#         if n >= m:
#             return 1
#         else:
#             return 0
#     elif ineq == '<' and eq =='=':
#         if n <= m:
#             return 1
#         else:
#             return 0
#     elif ineq == '>' and eq =='!':
#         if n > m:
#             return 1
#         else:
#             return 0
#     elif ineq == '<' and eq =='!':
#         if n < m:
#             return 1
#         else:
#             return 0
        
# # 위 풀이를 eval함수를 이용하여 풀 수 있다.
# def solution(ineq, eq, n, m):
#     return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))

# 마지막 두 원소
def solution(num_list):
   if num_list[-1] > num_list[-2]:
      return num_list + [(num_list[-1] - num_list[-2])]
   else:
      return num_list + [(num_list[-1] * 2)]
   
# 수 조작하기
def solution(n, control):

    for c in control:
        if c == 'w':
           n += 1
        elif c == 's':
           n -= 1
        elif c == 'd':
           n += 10
        elif c == 'a':
           n -= 10
        else: 
           print('fail')
    return n

# 이어 붙인 수
def solution(num_list):
    str1,str2 = '',''
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            str1 += str(num_list[i])
        else:
            str2 += str(num_list[i])
    return int(str1)+int(str2)

# 주사위 게임2
def solution(a, b, c):
    score = 0
    if (a != b) and (a != c) and (b != c):
        score = a+b+c
    elif (a == b) and (b == c):
        score = (a+b+c) + (a*a + b*b + c*c) + (a**3 + b**3 + c**3)
    else:
        score = (a+b+c) + (a*a + b*b + c*c)
    return score

# 등차수열의 특정한 항만 더하기
def solution(a, d, included):
    result = 0
    for i in range(len(included)):
        # i번째 항의 값을 구합니다.  term은 반복문 돌아갈 때마다 값이 변함.
        term = a + (d * i)
        # included[i]가 True인 경우만 result에 더합니다.
        if included[i]:
            result += term
    return result
