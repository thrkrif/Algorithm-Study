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

# # 마지막 두 원소
# def solution(num_list):
#    if num_list[-1] > num_list[-2]:
#       return num_list + [(num_list[-1] - num_list[-2])]
#    else:
#       return num_list + [(num_list[-1] * 2)]
   
# # 수 조작하기
# def solution(n, control):

#     for c in control:
#         if c == 'w':
#            n += 1
#         elif c == 's':
#            n -= 1
#         elif c == 'd':
#            n += 10
#         elif c == 'a':
#            n -= 10
#         else: 
#            print('fail')
#     return n

# # 이어 붙인 수
# def solution(num_list):
#     str1,str2 = '',''
#     for i in range(len(num_list)):
#         if num_list[i] % 2 == 0:
#             str1 += str(num_list[i])
#         else:
#             str2 += str(num_list[i])
#     return int(str1)+int(str2)

# # 주사위 게임2
# def solution(a, b, c):
#     score = 0
#     if (a != b) and (a != c) and (b != c):
#         score = a+b+c
#     elif (a == b) and (b == c):
#         score = (a+b+c) + (a*a + b*b + c*c) + (a**3 + b**3 + c**3)
#     else:
#         score = (a+b+c) + (a*a + b*b + c*c)
#     return score

# # 등차수열의 특정한 항만 더하기
# def solution(a, d, included):
#     result = 0
#     for i in range(len(included)):
#         # i번째 항의 값을 구합니다.  term은 반복문 돌아갈 때마다 값이 변함.
#         term = a + (d * i)
#         # included[i]가 True인 경우만 result에 더합니다.
#         if included[i]:
#             result += term
#     return result

# # 코드 처리하기
# def solution(code):
#     mode = 0
#     ret = ''
#     for idx in range(len(code)):
#         if mode == 0:
#             if code[idx] == '1':
#                 mode = 1
#             else:
#                 if idx % 2 == 0:
#                     ret += code[idx]
#         else:
#             if code[idx] == '1':
#                 mode = 0
#             else:
#                 if idx % 2 == 1:
#                     ret += code[idx]
#     if ret == '':
#         ret = 'EMPTY'
#     return ret

# 문자열 정수의 합
# 그냥 문자열 for문 돌리고 int 취해서 더해도 됐었음,,

# def solution(num_str):
#     num_str = [index for index in num_str]
#     num_str = [int(i) for i in num_str]
#     answer = 0
#     for i in num_str:
#         answer += i

#     return answer 

""" num_str = input()
num_str = [index for index in num_str]
num_str = [int(i) for i in num_str]
print(num_str) """


""" num_str = input()
sum = 0
for index in num_str:
    n = int(index)
    print(n)
    sum += n
print(sum) """

# # 뒤에서 5등 위로
# def solution(num_list):
#     num_list.sort()
#     return num_list[5:]

# # 배열의 길이에 따라 다른 연산하기
# def solution(arr, n):
#     if len(arr) % 2 == 1:
#         for i in range(len(arr)):
#             arr[::2] += 27

# from random import *
# for i in range(10):
#     print(randint(1,100)) # 1~100 중에 무작위로 출력

# # 배열 비교하기
# def solution(arr1, arr2):
#     sum1,sum2 = 0,0

#     if len(arr1) > len(arr2):
#         return 1
#     elif len(arr1) < len(arr2):
#         return -1
#     # len(arr1) == len(arr2)
#     else:
#         for i in range(len(arr1)):
#             sum1 += arr1[i]
#             sum2 += arr2[i]
#         if sum1 > sum2:
#             return 1
#         elif sum1 < sum2:
#             return -1
#         else:
#             return 0
        
# 배열의 원소만큼 추가하기
def solution(arr):
    answer = []
    
    for i in arr:
        for data in range(i):
            answer.append(i)

    return answer

arr = [5,1,4]
print(solution(arr))

# 배열의 원소만큼 추가하기2
# 1에서는 반복문을 두 번 이용헤서 시간이 오래걸린다.
def solution(arr):
    answer = []
    
    for i in arr:
        answer += [i] * i

    return answer

arr = [5,1,4]
print(solution(arr))

# 문자열 바꾸기
def solution(rny_string):
    answer = rny_string.replace('m', 'rn')
    return answer

# 문자열 바꿔서 찾기
# def solution(myString, pat):
    
#     translate_string = myString.translate(str.maketrans("AB","BA"))
    
#     if pat in translate_string:
#         return 1
#     else:
#         return 0

# # 번외로 pat을 바꾸기
# def solution2(myString, pat):

#     return  int(''.join(["B" if i == 'A' else 'B' for i in pat]) in myString)


# h = "AAABBB"
# # table = str.maketrans("AB","BA")
# table = h.maketrans("AB","BA")  # 출력 결과로 딕셔너리가 나온다. translate와 함께 사용한다.
# # h = h.translate(table)
# print(table)

# # 소문자로 바꾸기
# def solution(myString):
#     myString = myString.lower()
#     return myString

# # 대문자로 바꾸기
# def solution(myString):
#     answer = myString.upper()
#     return answer

# 원하는 문자열 찾기
def solution(myString, pat):
    myString_copy = myString.lower()
    pat_copy = pat.lower()

    if pat_copy in myString_copy:
        return 1
    else:
        return 0
    
# 공백으로 구분하기
def solution(my_string):
    answer = my_string.split('')
    return answer

# 특정한 문자를 대문자로 바꾸기
def solution(my_string, alp):
    return ''.join([i.upper() if i == alp else i for i in my_string])

# 특정한 문자를 대문자로 바꾸기 replace가 더 났다.
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())

# 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    for i in range(len(strArr)):
        if i % 2 == 0:
            strArr[i] = strArr[i].lower()
        else:
            strArr[i] = strArr[i].upper()
    
    return strArr

# 길이에 따른 연산

def solution(num_list):
    sum1,sum2 = 0,1
    if len(num_list) >= 11:
        for i in range(len(num_list)):
            sum1 += num_list[i]
        return sum1    
    else:
        for i in range(len(num_list)):
            sum2 *= num_list[i]
        return sum2

# A 강조하기

def solution(myString):
    return myString.lower().replace("a","A")

# 조건에 맞게 수열 변환하기 1

def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and  i % 2 == 0:
            answer.append(i/2)
        elif i <50 and i % 2 == 1:
            answer.append(i*2)
        else:
            answer.append(i)
    return answer

# n보다 커질 때까지 더하기

def solution(numbers, n):
    sum = 0
    for i in numbers:
        sum += i
        if sum > n:
            return sum
    
    return 0

# 할 일 목록
def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        if finished[i] == False:
            answer.append(todo_list[i])

    return answer

# 공백으로 구분하기 2
def solution(my_string):
    answer = my_string.split()
    return answer

# 5명씩
def solution(names):
    answer = names[::5]
    return answer

# n개 간격의 원소들
def solution(num_list, n):
    answer = num_list[::n]
    return answer

# n 번째 원소까지
def solution(num_list, n):
    answer = num_list[:n]
    return answer

# 순서 바꾸기
def solution(num_list, n):
    answer = num_list[n:] + num_list[:n]
    return answer

# n 번째 원소부터
def solution(num_list, n):
    answer = num_list[n-1:]
    return answer

# 첫 번째로 나오는 음수
def solution(num_list):
    for x,y in enumerate(num_list):
        if y < 0:
            return x
    return -1

# 카운트 다운
def solution(start_num, end_num):
    answer = []
    for i in range(start_num,end_num,-1):
        answer.append(i)
    return answer

# 배열 만들기 1
def solution(n, k):
    
    return [i for i in range(k,n+1,k)]

# 접두사인지 확인하기
# index 0 부터 확인
def solution(my_string, is_prefix):
        for i in len(is_prefix):
            if my_string[i] == is_prefix[i]:
                return 1
        return 0

# 문자열의 앞의 n글자
def solution(my_string, n):
    
    item  = [my_string[i] for i in range(n)]
    
    return ''.join(item)

# 문자열 앞의 n글자 훨씬 더 쉬운 버전 / 문자열도 슬라이싱 가능함
def solution(my_string, n):
    return my_string[:n]


# 문자열의 뒤의 n글자
def solution(my_string, n):
    return my_string[-n:]

# # 부분 문자열 이어 붙여 문자열 만들기
# def solution(my_strings, parts):
#     answer = ''
#     for i in range(len(my_strings)):
#         for s,e in parts:
#             answer += my_strings[s:e+1]

#     return answer

# 글자 이어 붙여 문자열 만들기
def solution(my_string, index_list):
    answer = [my_string[i] for i in index_list]
    return ''.join(answer)

# 배열의 원소 삭제하기
def solution(arr, delete_list):
    
    for i in delete_list:
        if i in arr:
            arr.remove(i)

    return arr

# 카운트 업
def solution(start_num, end_num):
    answer = []
    count = 0
    for i in range(end_num - start_num + 1):
        answer.append(start_num + count)
        count += 1
    return answer

# 부분 문자열
def solution(str1, str2):
    
    return 1 if str1 in str2 else 0

# 부분 문자열2
def solution(str1, str2):
    
    return int(str1 in str2)


# 홀수 vs 짝수
def solution(num_list):
    odd = num_list[::2]
    even = num_list[1::2]
    
    return sum(odd) if sum(odd) > sum(even) else sum(even)

# 홀수 vs 짝수2
def solution(num_list):
    odd = num_list[::2]
    even = num_list[1::2]
    
    return max(sum(odd), sum(even))

# 정수 찾기
def solution(num_list, n):
    
    return int(n in num_list)

# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    answer = [i * k if k % 2 == 1 else i + k for i in arr]
    return answer

# 간단한 식 계산하기
def solution(binomial):
    a = binomial.split()
    num1, num2 = int(a[0]), int(a[2])
    if a[1] == '+':
        return num1 + num2
    elif a[1] == '-':
        return num1 - num2
    elif a[1] == '*':
        return num1 * num2
    
# # l로 만들기 안되는 이유
def solution(myString):
    for item in myString:
        if item < 'l':
            myString.replace(item, 'l')
    return myString

# l로 만들기
def solution(myString):
        
    return ''.join(['l' if i < 'l' else i for i in myString])
        
# 가까운 1 찾기
def solution(arr, idx):

    for index in range(len(arr)):
        if idx <= index and arr[index] == 1:
            return index

    return -1

# 배열 만들기 3
def solution(arr, intervals):
    answer = []
    for i,j in intervals:
        answer += arr[i:j+1]
    return answer

# 9로 나눈 나머지
def solution(number):
    answer = 0
    for i in number:
        answer += int(i)
    return answer % 9

# 수 조작하기 2
def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        if numLog[i] == numLog[i+1] - 1:
            answer += 'w'
        elif numLog[i] == numLog[i+1] + 1:
            answer += 's'
        elif numLog[i] == numLog[i+1] - 10:
            answer += 'd'
        elif numLog[i] == numLog[i+1] + 10:
            answer += 'a'
        else:
            return False
    return answer

# 콜라츠 수열 만들기
def solution(n):
    answer = []
    
    while n != 1:
        if n % 2 == 0:
            answer.append(n)
            n = n//2
        else:
            answer.append(n)
            n = 3 * n + 1
    answer.append(n)

    return answer

# 문자열 잘라서 정렬하기
def solution(myString):
    answer = myString.split('x')
    answer = [i for i in answer if i ]
    answer.sort()
    return answer

# 리스트 자르기
def solution(n, slicer, num_list):
    if n == 1:
        return num_list[0:slicer[1] + 1]
    elif n == 2:
        return num_list[slicer[0]:]
    elif n == 3:
        return num_list[slicer[0]:slicer[1] + 1]
    elif n == 4:
        return num_list[slicer[0]:slicer[1] + 1:slicer[2]]
    else:
        return -1
    
# 날짜 비교하기
def solution(date1, date2):
    if date1[0] < date2[0]:
        return 1
    elif date1[0] == date2[0]:
        if date1[1] < date2[1]:
            return 1
        elif date1[1] == date2[1]:
            if date1[2] < date2[2]:
                return 1
    return 0

# 글자 지우기
def solution(my_string, indices):
    answer = my_string.split('')
    for i in indices:
        del answer[i]
    return ''.join(answer)

# 커피 심부름
def solution(order):
    money = 0
    for i in order:
        if i == "iceamericano"  or i == "americanoice" or  i == "americano" or i == "anything":
            money += 4500
        elif i == "hotamericano" or i == "americanohot":
            money += 4500
        else:
            money += 5000
    
    return money

# 2의 영역
def solution(arr):
    answer = [i for i in range(len(arr)) if arr[i] == 2]   # arr[i] == 2 인 i의 index들을 추출
    if len(answer) == 0:
        return [-1]
    elif len(answer) == 1:
        return [arr[answer[0]]]
    else:
        return arr[answer[0]:answer[-1] + 1]
    
# 1로 만들기 --> 실행시간 초과로 실패
def solution(num_list):
    count = 0
    for i in num_list:
        while i != 1:
            i = i // 2
            count += 1
    return count

# 문자열 뒤집기
def solution(my_string, s, e):
    
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

# 배열 만들기 5
def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        if int(i[s:s+l]) > k:
            answer.append(int(i[s:s+l]))
    return answer

# 간단한 논리 연산
def solution(x1, x2, x3, x4):
    
    return (x1 or x2) and (x3 or x4)

# 두 수의 합
def solution(a, b):
    
    return str(int(a) + int(b))

# qr code
def solution(q, r, code):
    result = [code[i] for i in range(len(code)) if i % q == r]
    
    return ''.join(result)

# 부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        answer += my_strings[i][parts[i][0]:parts[i][1]+1]

    return answer

# 수열과 구간 쿼리 2  --> 모르겠음..
# def solution(arr, queries):
#     for (s,e,k) in queries:
#         answer = [min(i) if i > k else -1 for i in arr[s:e+1]]
    
#     return answer

# 수열과 구간 쿼리 3
def solution(arr, queries):
    
    for i,j in queries:
        arr[i],arr[j] = arr[j],arr[i]
    return arr

# 배열 만들기 2
def solution(l, r):
    answer = [i for i in range(l,r+1) if all(c in '05' for c in str(i))]

    return answer if answer else [-1]

# 배열 만들기 4
def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                del stk[-1]
    return stk

# 접두사인지 확인하기
def solution(my_string, is_prefix):
        result = []
        for i in range(len(my_string)):
            result.append(my_string[0:i])
        if is_prefix in result:
            return 1
        else:
            return 0

# 접미사인지 확인하기 1. endswith() 함수 이용
def solution(my_string, is_suffix):
    
    return int(my_string.endswith(is_suffix))

# 접미사인지 확인하기
def solution(my_string, is_suffix):
    result = []
    my_string = my_string[::-1]
    for i in range(len(my_string)):
        result.append(my_string[0:i])
    if is_suffix in result:
        return 1
    else:
        return 0
    
# 접미사 배열
def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    answer.sort()
    return answer

# 꼬리 문자열
def solution(str_list, ex):
    answer = ''
    for i in range(len(str_list)):
        if ex not in str_list[i]:
            answer += str_list[i]
    return answer

# 부분 문자열인지 확인하기
def solution(my_string, target):
    
    if target in my_string:
        return 1
    return 0

# 0 떼기
def solution(n_str):
    
    for i in range(len(n_str)):
        if n_str[i] != '0':
            return n_str[i:]
        
# 배열의 길이에 따라 다른 연산하기
def solution(arr, n):
    
    if len(arr) % 2 == 0:
        for i in range(1,len(arr),2):
            arr[i] += n
    else:
        for i in range(0,len(arr),2):
            arr[i] += n
    return arr

# ad 제거하기
def solution(strArr):
    answer = [i for i in strArr if 'ad' not in i]
    return answer

# 특별한 이차원 배열 1
def solution(n):
    answer = []
    for i in range(n):
        answer.append([])
        for j in range(n):
            if i == j:
                answer[i].append(1)
            else:
                answer[i].append(0)

    return answer

# 주사위 게임 1
def solution(a, b):
    if a % 2 == 1 and b % 2 == 1:
        return a*a + b*b
    elif a % 2 == 0 and b % 2 == 0:
        return abs(a-b)
    else:
        return 2 * (a + b)
    
# 특별한 이차원 배열 2        --> 왜 오답이 나올까?
def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                return 1
    return 0

# 특별한 이차원 배열 2
def solution(arr):
    answer = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                answer.append(1)
            else:
                answer.append(0)
    if 0 in answer:
        return 0
    else:
        return 1
    
# 이차원 배열 대각선 순회하기
def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                answer += board[i][j]
    return answer

# 세로 읽기
def solution(my_string, m, c):
    answer = my_string[c-1::m]
    
    return answer

# 빈 배열에 추가, 삭제하기
def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i]:
            answer.extend([arr[i]] * (arr[i] * 2))
        else:
            del answer[-arr[i]:]
    return answer

# 문자열이 몇 번 등장하는지 세기
def solution(myString, pat):
    count = 0
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            count += 1
    return count

# 수열과 구간 쿼리 1
def solution(arr, queries):
    
    for s,e in queries:
        for i in range(s,e+1):
            arr[i] += 1
    return arr

# 배열의 길이를 2의 거듭제곱으로 만들기     다른 사람 풀이 보면서 공부 한번 더하기
def solution(arr):
    
    for i in range(11):
        if len(arr) == 2 ** i:
            return arr
        elif len(arr) > 2 ** i and len(arr) < 2 ** (i+1):
            for j in range(2**(i+1)-len(arr)):
                arr.append(0)
            return arr
    
# 문자열 묶기
def solution(strArr):
    count1, count2, count3 = 0,0,0
    for i in strArr:
        if len(i) == 1:
            count1 += 1
        elif len(i) == 2:
            count2 += 1
        elif len(i) == 3:
            count3 += 1
            
    return max(count1,count2,count3)

# 조건에 맞게 수열 변환하기 2
def solution(arr):
    result = []
    result.append(arr)
    """
    result라는 이차원 리스트를 만들고 result[x] = result [x+1] 이면 x를 return 하도록 할 것임
    """
    my_list = []
    for num in arr:
        if num >= 50 and num % 2 == 0:
            num = num // 2
        elif num < 50 and num % 2 == 1:
            num = num*2 + 1
        my_list.append(num)
    result.append(my_list)
    # my_list라는 리스트에 for문의 요소들을 저장하고 이 리스트를 result에 추가한다. 즉 이것은 result[1]이 된다.
    # 이 과정을 result[x] == result[x+1] 이 될 때까지 반복하게 하는 반복문을 만들면 된다.

    x = 0 # 위에서 0,1을 만들어 놨으므로 비교 시작한다.
    while result[x] != result[x+1]:
        my_list = []
        for num in arr:
            if num >= 50 and num % 2 == 0:
                num /= 2
            elif num < 50 and num % 2 == 1:
                num = num*2 + 1
        my_list.append(num)
    result.append(my_list)

    return x

# 문자 개수 세기
def solution(my_string):
    answer = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)] 
    lst = [0] * 52
    
    for i in range(len(answer)):
        for j in my_string:
            if answer[i] == j:
                lst[i] += 1
    
    return lst

# 배열 만들기 6
def solution(arr):
    
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif len(stk) >= 1:
            if stk[-1] == arr[i]:
                stk.pop()
                i += 1
            else:
                stk.append(arr[i])
                i += 1

    return  stk if len(stk) >= 1 else [-1]

# 왼쪽 오른쪽 내가 짠 코드인데 오류가 있음
def solution(str_list):
    
    if 'l' and 'r' not in str_list:
        return []

    if str_list.index('l') < str_list.index('r'):
        return str_list[:str_list.index('l')]
    elif str_list.index('l') > str_list.index('r'):
        return str_list[str_list.index('r') + 1:]
    else:
        return []
    
# 왼쪽 오른쪽 수정본
# l,r 둘 중 하나만 있는 경우도 생각해야해서 l과 r의 위치를 없으면 inf로 초기화 해야함
def solution(str_list):
    # 'l'과 'r'이 str_list에 모두 없는 경우 빈 리스트 반환
    if 'l' not in str_list and 'r' not in str_list:
        return []
    
    # 'l'과 'r'의 위치를 초기화
    l_index = str_list.index('l') if 'l' in str_list else float('inf')
    r_index = str_list.index('r') if 'r' in str_list else float('inf')
    
    # 'l'이 더 먼저 나오는 경우
    if l_index < r_index:
        return str_list[:l_index]
    # 'r'이 더 먼저 나오는 경우
    elif r_index < l_index:
        return str_list[r_index + 1:]



# 수열 구간과 쿼리2
def solution(arr, queries):
	answer = []
	for (s,e,k) in queries:
		answer += [[arr[i] for i in range(s,e+1) if arr[i] > k]]
	return [min(i) if len(i) >= 1 else -1 for i in answer]

# 수열과 구간 쿼리 4
def solution(arr, queries):
    for (s,e,k) in queries:
        for i in range(s,e+1):
            if i % k == 0:
                arr[i] += 1
    return arr

# 배열 만들기 2
def solution(l, r):
    answer = [ i for i in range(l,r+1) if all( char in '05' for char in str(i))]
    return answer if answer else [-1]

# 그림 확대
def solution(picture, k):
    # 1. 가로 확대
    result = []
    for i in range(len(picture)):
        answer = ''             # +=을 하면 0번째 행의 글자가 1번째 행이랑 합쳐지고 그 다음엔 2번째랑 합쳐지고... 하므로 한번 돌때마다 초기화
        for j in picture[i]:    # j는 str 형식으로 들어감.
            answer += j * k     # 한 행을 수행한다.
        # 2. 세로 확대    
        for m in range(k): 
            result.append(answer)   # 한 행을 마치면 리스트에 추가한다.
        
    return result

# 전국 대회 선발 고사
def solution(rank, attendance):
    result = []
    for i in range(len(rank)):
        if attendance[i] == True:
            result.append(rank[i])
    result.sort()
    return 10000 * result[0] + 100 * result[1] + result[2]

# 배열 조각하기
def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    return arr