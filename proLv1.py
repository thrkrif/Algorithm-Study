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
    return n * 12000 + (k - n // 10) * 2000

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

# 암호 해독
def solution(cipher, code):
    return ''.join([cipher[i] for i in range(len(cipher)) if (i+1) % code == 0])

# 가장 큰 수 찾기
def solution(array):
    
    return [max(array), array.index(max(array))]

# n의 배수 고르기
def solution(n, numlist):
    
    return [i for i in numlist if i % n == 0]

# 특정 문자 제거하기
def solution(my_string, letter):
    
    return ''.join([i for i in my_string if letter not in i]) 

# 자릿수 더하기
def solution(n):
    
    sum = 0
    while n > 9:
        sum += n % 10
        n = n // 10
    sum += n
    
    return sum

# 짝수의 합
def solution(n):
    return sum([i for i in range(n+1) if i % 2 == 0])

# 짝수의 합
def solution(n):
    return sum(range(2,n+1,2))

# 머쓱이보다 키 큰 사람
def solution(array, height):
    answer = [i for i in array if i > height]
    return len(answer)

# 피자 나눠 먹기 (1)
def solution(n):
    return  (n // 7) if n % 7 == 0 else (n // 7) + 1

# 배열의 유사도
def solution(s1, s2):
    count = 0
    for i in s1:
        for j in s2:
            if i == j:
                count += 1
    return count

# 배열의 유사도
# 집합을 이용하여 쉽게 풀 수 있다.
def solution(s1, s2):
     return len(set(s1) & set(s2)) 


# 최댓값 만들기(1)
def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]

# 세균 증식
def solution(n, t):
    return n * (2**t)

# 직각삼각형 출력하기
n = int(input())
for i in range(n):
    print('*' * (i+1))

# 최댓값 만들기 (2)
"""
조건 1. 최댓값이 되려면 두 수 모두 양수 or 음수여야함.
"""
def solution(numbers):
    sort_numbers = sorted(numbers)
    max1 = sort_numbers[0] * sort_numbers[1] 
    max2 = sort_numbers[-1] * sort_numbers[-2]
    return max(max1,max2)

# 점의 위치 구하기
def solution(dot):
    if dot[0] > 0 and dot[1] > 0 :
        return 1
    elif dot[0] < 0 and dot[1] > 0 :
        return 2
    elif dot[0] < 0 and dot[1] < 0 :
        return 3
    else:
        return 4
    
# 가위 바위 보
def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        if i == '5':
            answer += '2'
    return answer

# 순서쌍의 개수
def solution(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count

# 삼각형의 완성조건 (1)
def solution(sides):
    long = max(sides)
    sides.pop(sides.index(long))
    if long < sum(sides):
        return 1
    else:
        return 2
    
# 피자 나눠 먹기 (3)
def solution(slice, n):
    return (n-1) // slice + 1

# 피자 나눠 먹기 (2)
def solution(n):
    i = 1
    while True:
        if (n * i) % 6 == 0:
            return (n * i) / 6
        i += 1

# 369게임
"""
3,6,9 가 들어있으면 박수를 한 번씩 쳐야한다. 29423은 9,3 이 있으므로 두번 쳐야한다.
"""

def solution(order):
    count = 0
    for i in str(order):
        if i == '3' or i == '6' or i == '9':
            count += 1
    return count

# 문자열 정렬하기 (2)
"""
upper, lower는 
"""
def solution(my_string):
    my_string = my_string.lower()
    return ''.join(sorted(my_string))

# 배열 회전시키기
def solution(numbers, direction):
    if direction == "right":
        return  [numbers.pop()]+ numbers[:] 
    elif direction == "left":
        return numbers[1:] + [numbers[0]]
    
# 문자열 정렬하기 (1)
def solution(my_string):
     return sorted([int(i) for i in my_string if i.isdigit()])

# 제곱수 판별하기
def solution(n):
    for i in range(1,n//2):
        if i ** 2 == n:
            return 1
    return 2

# 대문자와 소문자
def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        elif i.islower():
            answer += i.upper()
    return answer

# 주사위의 개수
def solution(box, n):
    return (box[0] // n) * (box[1] // n) * (box[2] // n)

# 모음 제거
def solution(my_string):
    answer = ''
    for i in my_string:
        if i == 'a':
            continue
        elif i == 'i':
            continue
        elif i == 'e':
            continue
        elif i == 'o':
            continue
        elif i == 'u':
            continue
        else:
            answer += i
    return answer

# 약수 구하기
def solution(n):
    return [i for i in range(1,n+1) if n % i == 0]

# A로 B 만들기
def solution(before, after):
    before = before[::-1]
    if before == after:
        return 1
    else:
        return 0
    

# 인덱스 바꾸기 슬라이싱 기법 이용
def solution(my_string, num1, num2):
    return my_string[:num1] + my_string[num2] + my_string[num1+1:num2] + my_string[num1] + my_string[num2+1:]

# 인덱스 바꾸기 리스트 이용
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)

# 중복된 문자 제거
def solution(my_string):
    answer = ''
    for i in my_string:
        if i in answer:
            continue
        answer += i
    return answer

# 최빈값 구하기
def solution(array):
    answer = [0] * 1000
    for i in array:
        answer[i] += 1
    result = max(answer)
    count = 0
    for i in range(len(answer)):
        if answer[i] == result:
            count += 1
    return -1 if count >= 2 else answer.index(result)

# 최빈값 구하기2
def solution(array):
    answer = [0] * 1000
    for i in array:
        answer[i] += 1
    result = max(answer)
    
    return -1 if answer.count(result) >= 2 else answer.index(result)

# 숫자 찾기
def solution(num, k):
    num_list = list(str(num))
    if str(k) in num_list:
        return num_list.index(str(k)) + 1
    return -1

# 외계행성의 나이
def solution(age):
    dic = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h' ,8:'i', 9:'j'}
    answer = ''
    for i in str(age):
        answer += dic[int(i)]
    return answer

# k의 개수
def solution(i, j, k):
    sum = 0 
    for _ in range(i,j+1):
        sum += str(_).count(str(k))
    return sum

# A로 B 만들기
"""
문자가 똑같이 들어 있으면 (어떤 문자가, 몇개 들었는지) 확인 가능하다.
"""
def solution(before, after):
    answer1,answer2 = {},{}
    for i in before:
        if i not in answer1:
            answer1[i] = before.count(i)
    for j in after:
        if j not in answer2:
            answer2[j] = after.count(j)
    
    return 1 if sorted(answer1.items()) == sorted(answer2.items()) else 0

# A로 B 만들기 다른 풀이
def solution(before, after):
    return 1 if sorted(before)==sorted(after) else 0

# 7의 개수
def solution(array):
    result = 0
    for i in array:
        result += str(i).count('7')
    return result

# 한 번만 가능한 문자
def solution(s):
    result = ''
    for i in s:
        if s.count(i) == 1:
            result += i
    return [] if not result else ''.join(sorted(result))

# 컨트롤 제트
def solution(s):
    new_s = s.split(' ')
    result = 0
    for i in range(len(new_s)):
        if new_s[i] == 'Z':
            result -= int(new_s[i-1])
        else:
            result += int(new_s[i])
    return result

# 컨트롤 제트 stack 이용
def solution(s):
    stack = []
    for i in s.split():
        if i != 'Z':
            stack.append(int(i))
        else:
            if stack:
                stack.pop()
    return sum(stack)

# 문자열 계산하기
def solution(my_string):
    answer = my_string.split(' ')
    result = int(answer[0])
    for i in range(1,len(answer),2):
        operator = answer[i]
        number = int(answer[i+1])
        if operator == '+':
            result += number
        elif operator == '-':
            result -= number

    return result

# 영어가 싫어요
def solution(numbers):
    numbers = numbers.replace('zero','0')
    numbers = numbers.replace('one','1')
    numbers = numbers.replace('two','2')
    numbers = numbers.replace('three','3')
    numbers = numbers.replace('four','4')
    numbers = numbers.replace('five','5')
    numbers = numbers.replace('six','6')
    numbers = numbers.replace('seven','7')
    numbers = numbers.replace('eight','8')
    numbers = numbers.replace('nine','9')
    
    return int(numbers)

# 구슬을 나누는 경우의 수
def solution(balls, share):
    mol = 1 # 분자
    denom = 1 # 분모
    for i in range(balls-share+1,balls+1):
        mol *= i
    for j in range(2,share+1):
        denom *= j
    return mol / denom

# 삼각형의 완성조건 (2)
"""
1. sides에 있는 두 수 중에 가장 큰 수가 빗변이 되는 경우.
2. sides에 포함 되어 있지 않는 것이 빗변이 되는 경우
"""
def solution(sides):
    # 1
    count = 0
    max = sides.pop(max(sides))
    for i in range(max - sides[0],max):


    return answer

# 팩토리얼
def solution(n):
    i = 1
    fac = 1
    while(n >= fac):
        fac *= i
        i += 1
    return i-2

# 외계어 사전
def solution(spell, dic):
    for i in dic:
        if sorted(spell) == sorted(list(i)):
            return 1
    return 2

# 분수의 덧셈
def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    denom,numer = result(denom,numer)
    answer.append(denom)
    answer.append(numer)
    return answer

def result(denom,numer):
    for i in range(2,denom+1):
        if denom % i == 0 and numer % i == 0:
            denom //= i
            numer //= i
            return result(denom,numer)
    return denom,numer

# 합성수 찾기
def solution(n):
    result = 0
    for i in range(4,n+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
        if count >= 3:
            result += 1
    return result

# 숨어있는 숫자의 덧셈 (2) -> 런타임 에러 발생
def solution(my_string):

    my_string = my_string.translate(str.maketrans('abcdefghizklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',' ' * len('abcdefghizklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')))
    numbers = my_string.split()
    
    return sum([int(i) for i in numbers])

# 모스부호(1)
def solution(letter):
    morse = {       
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    for key, value in morse.items():
        if key in letter:
            letter = letter.replace(key,value)
    return letter

# 진료순서 정하기
def solution(emergency):
    answer = [0] * len(emergency)
    rank = 1
    
    while(emergency != [0] * len(emergency)):
        index = emergency.index(max(emergency)) # 최댓값의 인덱스
        answer[index] = rank    # 순위를 집어넣고 rank 증가
        rank += 1
        emergency[index] = 0
    return answer

# 캐릭터의 좌표
"""
1. 보드 제한 없다고 생각하고 풀어보기
2. 보드 제한 있이, [7,9]라면 좌우로 3, 위 아래로 4 까지 이동 가능
"""

def solution(keyinput, board):
    answer = [0,0]
    new_board = [[0,0],[0,0]]
    new_board[0][0] = -(board[0] // 2)
    new_board[0][1] = board[0] // 2
    new_board[1][0] = -(board[1] // 2)
    new_board[1][1] = board[1] // 2

    for i in keyinput:
        if i == 'left':
            answer[0] += -1
        elif i == "right":
            answer[0] += 1
        elif i == 'up':
            answer[1] += 1
        elif i == 'down':
            answer[1] += -1
        else:
            print("잘못된 입력입니다.")

    if abs(new_board[0][0]) < abs(answer[0]):
        if answer[0] < 0:
            answer[0] = new_board[0][0]
        elif answer[0] > 0:
            answer[0] = new_board[0][1]
        
    
    if abs(new_board[1][0]) < abs(answer[1]):
        if answer[1] < 0:
            answer[1] = new_board[1][0]
        elif answer[1] > 0:
            answer[1] = new_board[1][1]

    return answer

# 로그인 성공?
def solution(id_pw, db):
    answer = ''
    for i in db:
        if i == id_pw:
            return 'login'
        else:   # id_pw가 맞지 않는 경우 --> 여기서 오류가 발생함. 중간에 아이디만 맞는게 있어서 answer = 'wrong pw'가 되어도
                # 마지막에 아이디 비밀번호가 틀린게 나온다면 answer = 'fail'이 저장됨. 이 문제를 어떻게 해결해야 할까?? 
            if i[0] == id_pw[0]:
                answer = 'wrong pw'
            else:
                answer = 'fail'
                
    return answer


def solution(id_pw, db):
    answer = 'fail' # 처음부터 answer를 fail로 지정해주면 된다.
    for i in db:
        if i == id_pw:
            return 'login'
        else:   
            if i[0] == id_pw[0]:
                answer = 'wrong pw'
                
    return answer

# 코드 분석하기
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"

# 등수 매기기
def solution(score):
    score_avg = []
    for i,j in score:
        score_avg.append((i+j) / 2.0)
    sorted_score_avg = sorted(score_avg,reverse=True) 
    return [(sorted_score_avg.index(k)+1) for k in score_avg] # 2로 나누지 않았어도 상관 없었겠다.

# 치킨 쿠폰
"""
치킨 1마리당 쿠폰 1 , 서비스 치킨에도 쿠폰 발급
쿠폰 10장에 치킨 1마리
1. 1081마리 시킴 -> 쿠폰 1081장 -> 쿠폰 : 1081 // 10 = 108(몫) + 1081 % 10 = 1(나머지) = 109개 
2. 쿠폰 108개로 치킨 10마리 시킴(쿠폰 10개) + 남은쿠폰 8 + 1 -> 쿠폰: 109 // 10 = 10(몫) + 19 % 10 = 9(나머지) -> 19개
3. 쿠폰 10개로 치킨 1마리 시킴(쿠폰 1개) + 남은 쿠폰 9개 -> 19 // 10 = 1(몫) + 9 % 10 = 9(나머지) -> 10개
4. 쿠폰 10개로 치킨 1마리 시킴 -> 쿠폰 1개 남음, 끝 -> 10 // 10 = 1(몫) + 10 % 10 = 0(나머지) -> 1개

1. 치킨 108, 2. 치킨 10, 3. 치킨 1, 4. 치킨 1 --> 총 치킨 120(몫들의 합)
"""

def solution(chicken):
    coupon = chicken    # 초기 쿠폰의 수 1081장
    service_chicken = 0
    while(coupon >= 10):    # 쿠폰이 10장 미만이면 더이상 서비스 치킨을 먹을 수 없음
        service_chicken += coupon // 10
        coupon = coupon // 10 + coupon % 10
    return service_chicken

# 문자열 밀기
def solution(A, B):
    answer = 0
    a,b = list(A),list(b)
    for i in range(len(a)):
        if a == b:
            return i
        a = a[-1] + a[]

    return answer

# 다항식 더하기
def solution(polynomial):
    string_list = polynomial.split(' + ')
    sum = 0
    xsum = 0
    for i in string_list:
        if 'x' in i:
            if i == 'x':
                xsum += 1
            else:
                xsum += int(i.replace('x',''))
        else:
            sum += int(i)
    result = []
    if xsum != 0:
        if xsum == 1:
            result.append('x')
        else:
            result.append(f"{xsum}x")
    if sum != 0:
        result.append(str(sum))
    
    return ' + '.join(result)