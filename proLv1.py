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