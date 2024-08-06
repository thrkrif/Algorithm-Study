# 두 수의 합
def solution(num1, num2):

    return num1 + num2

# 두 수의 차
def solution(num1, num2):
    
    return num1 - num2

# 두 수의 곱
def solution(num1, num2):
    
    return num1 * num2

# 몫 구하기
def solution(num1, num2):
    
    return num1 // num2

# 두 수의 나눗셈
def solution(num1, num2):
    
    return int((num1 / num2) * 1000)

# 나머지 구하기
def solution(num1, num2):
    
    return num1 % num2

# 숫자 비교하기
def solution(num1, num2):
    
    return  1 if num1 == num2 else -1

# 배열 두 배 만들기
def solution(numbers):
    
    return [numbers[i] * 2 for i in range(len(numbers))]

# 배열의 평균값 --> 너무 어렵게 생각함
def solution(numbers):
    
    return sum([ numbers[i] / len(numbers) for i in range(len(numbers))])

# 배열의 평균값
def solution(numbers):
    return sum(numbers) / len(numbers)

# 각도기

def solution(angle):
    if angle > 0 and angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle > 90 and angle < 180:
        return 3
    elif angle == 180:
        return 4

# 각도기 문제를 이렇게도 푸나??
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer

# 나이 출력
def solution(age):
    
    return (2023 - age)

# 문자열 뒤집기
def solution(my_string):
    
    return my_string[::-1]

# 양꼬치
"""
양꼬치 n인분, 음료수 k인분, n == 10 일때마다 음료수 1개 공짜
"""
def solution(n, k):
    
    return 

# 편지
def solution(message):
    
    return len(message) * 2

# 배열 뒤집기
def solution(num_list):
    num_list.reverse()
    return num_list

# 짝수 홀수 개수
def solution(num_list):
    answer = []
    odd = [i for i in num_list if i % 2 == 1]
    even = [i for i in num_list if i % 2 == 0]
    answer.append(len(even))
    answer.append(len(odd))
    return answer

# 짝수 홀수 개수 더 쉽게
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1  # 인덱스 내에서도 연산이 가능하구나 %2로 하면 index는 0,1 밖에 안되니까 짝수이면 0에 count, 홀수이면 1에 count
    return answer

# 문자 반복 출력하기
def solution(my_string, n):
    
    return ''.join(i*n for i in my_string)

# 중복된 숫자 개수
def solution(array, n):
    count = 0
    for i in array:
        if i == n:
            count += 1
    return count    # 리스트 내장 함수 count를 썼으면 더 쉽게 풀이 가능했다. return array.count(n) 이면 끝

# 문자열안에 문자열
def solution(str1, str2):
    
    return 1 if str2 in str1 else 2

# 배열 원소의 길이
def solution(strlist):
    return [len(i) for i in strlist]

# 중앙값 구하기
def solution(array):
    array.sort()
    return array[len(array)//2]

# 짝수는 싫어요
def solution(n):
    answer = [i for i in range(n+1) if i % 2 == 1]
    return sorted(answer)

def solution(n):
    return [x for x in range(n + 1) if x % 2]   # 0은 False, 1은 True 이므로

# 피자 나눠 먹기 (1)
def solution(n):
    pizza  = n % 7 + 1
    return pizza

# 옷가게 할인 받기
def solution(price):
    
    if price > 0 and price < 100000:
        return price
    elif price >= 100000 and price < 300000:
        return (price * (0.95))
    elif price >= 300000 and price < 500000:
        return (price * (0.90))
    else:
        return (price * (0.80))
    
# 옷가게 할인 받기 items() 사용
def solution(price):
    discount = {500000:0.8, 300000:0.9, 100000:0.95, 0:1}
    for discount_price, distcount_rate in discount.items():
        if price >= discount_price:
            return int(price * distcount_rate)


# 아이스 아메리카노
def solution(money):
    ice = 5500
    change = money % ice
    count = money // ice
    return [count, change]

# 배열 자르기
def solution(numbers, num1, num2):
    
    return numbers[num1:num2+1]

# 개미 군단
def solution(hp):
    general = hp // 5
    soldier = (hp % 5) // 3
    work = (hp % 5) % 3 // 1
    
    return general + soldier + work

# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
     
    return sum([int(i) for i in my_string if i.isdecimal()])