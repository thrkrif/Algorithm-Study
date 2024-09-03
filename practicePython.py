# import copy

# # first = input()
# # second = input()
# # a = int(first)  / int(second)
# # b = '값은 {0}이다.'.format(a)
# # print(b)


# # digit1 = 10
# # digit2 = 2.2
# # digit3 = "Hi"
# # print(type(digit1))
# # print(type(digit2))
# # print(type(digit3))

# # first = int(input())
# # second = int(input())
# # print(first,second)
# # if(first > second):
# #     print(first)
# # else:
# #     print(second)

# #  세 개 값 중 최솟값 찾기
# # digit1 = int(input())
# # digit2 = int(input())
# # digit3 = int(input())

# # if digit1 < digit2:
# #     min = digit1
# # else:
# #     min = digit2

# # if min < digit3:
# #     print (min)
# # else:
# #     print (digit3)

# # mystr = "a man goes into the room..."
# # b = mystr.strip('.')
# # print(b)

# # code = '         000660\n            '
# # b = code.strip(' \n')
# # print(b)

# # # count
# # python_desc = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace."
# # print(python_desc.count('Python'))
# # print(python_desc.count('p'))

# # # indexing
# # letters = "python"
# # print(letters[1] + letters[3])



# # 2024 06 21

# # 집합 자료형

# """ s = set("Hello")
# print(s)

# a = [1,2,3,4]
# while a :
#     print(a.pop())

# a = [1,2,3]
# b = a.copy()
# c = a[:]
# d = a
# print(id(a),id(b),id(c),id(d))

# # swap 쉽게 구현 가능하다.
# a,b = 3,5
# print(a,b)
# a,b = b,a
# print(a,b)

# print('='*13)
# print('  과목  점수  ')
# print('='*13)
# a = {'국어' : '80', '영어' : '75', '수학' : '55'}
# print(a)
# sum = int(a['국어']) + int(a['수학']) + int(a['영어'])
# ave = sum / 3
# print('평균: ' + str(ave))

# a = "a:b:c:d"
# b = a.replace(':','#')
# print(b)

# data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(data_list[2][2] + data_list[2][1] + data_list[2][0])
#  """
# # 'M'의 개수 찾기
# dataset = ['Braund, Mr. Owen Harris',
# 'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
# 'Heikkinen, Miss. Laina',
# 'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
# 'Allen, Mr. William Henry',
# 'Moran, Mr. James',
# 'McCarthy, Mr. Timothy J',
# 'Palsson, Master. Gosta Leonard',
# 'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
# 'Nasser, Mrs. Nicholas (Adele Achem)',
# 'Sandstrom, Miss. Marguerite Rut',
# 'Bonnell, Miss. Elizabeth',
# 'Saundercock, Mr. William Henry',
# 'Andersson, Mr. Anders Johan',
# 'Vestrom, Miss. Hulda Amanda Adolfina',
# 'Hewlett, Mrs. (Mary D Kingcome) ',
# 'Rice, Master. Eugene',
# 'Williams, Mr. Charles Eugene',
# 'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
# 'Masselmani, Mrs. Fatima',
# 'Fynney, Mr. Joseph J',
# 'Beesley, Mr. Lawrence',
# 'McGowan, Miss. Anna "Annie"',
# 'Sloper, Mr. William Thompson',
# 'Palsson, Miss. Torborg Danira',
# 'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
# 'Emir, Mr. Farred Chehab',
# 'Fortune, Mr. Charles Alexander',
# 'Dwyer, Miss. Ellen "Nellie"',
# 'Todoroff, Mr. Lalio']

# """ count = 0
# for data in dataset:
#     for index in data:
#         if index == 'M':
#             count += 1
# print(count) """

# """
# # 0이 나온다. count는 요소에 'M'이 있는지 찾는것이다.
# dataset.count('M')
#  """


# # 24 06 23  조건문, 반복문

# """ a = 1 in [1,2,3]
# print(a)

# pocket = ['cellphone', 'money']
# if 'money' in pocket :
#     print('택시를 타고 가라')
# else:
#     print('걸어가라')

# print('택시를 타고 가라') if 'money' in pocket else print('걸어가라') """

# """ prompt = '''
# 1. Add
# 2. Del
# 3. List
# 4. Quit
# Enter number : ''' 

# number = 0
# while number <= 4:
#     print(prompt)
#     number = int(input()) """


# """ coffee = 10
# money = 3000
# price = 300
# while coffee > 0 and money > 0:
#     print("현재 잔액: %d원" % money)
#     print("%d원을 넣어주세요" % price)
#     money -= price
#     print('남은 잔액: %d원' % money)
#     print('현재 커피 수: %d' % coffee)
#     coffee -= 1
#     print('남은 커피 수: %d' % coffee)
#     print() """

# # 3의 배수를 뺀 나머지 출력
# """ a = 0
# while a < 10:
#     a = a + 1
#     if a % 3 == 0 : 
#         continue
#     print(a)
    
# for i in ['one', 'two', 'three']:
#     print(i)

# number = 0
# for grade in [61, 96, 30]:
#     number += 1
#     print("%d번 학생! " % number)
#     if grade >= 60 :
#         print("합격, 당신의 점수: %d" % grade)
#     else:
#          print("불합격, 당신의 점수: %d" % grade)

# add = 0
# for i in range(1,101):
#     add += i
# print(add)

# # 루프 끝나면 i 다시 초기화, 따라서 마지막 i = 100 + 100 = 200이 된다.
# for i in range(1,101):
#     i += i
# print(i)

# # 구구단 출력

# for i in range(1,10):
#     for j in range(1,10):
#         print(i*j, end=' ')
#     print()

# # 리스트 내포

# a = [1,2,3,4]
# result = [num * 3 for num in a if num % 2 ==0]
# print(result)

# gugu = [x*y for x in range(2,10)
#         for y in range(2,10)]
# print(gugu)

# i = 0
# while True:
#     i += 1
#     print('*' * i)
#     if i == 5:
#         break

# result = [num * 2 for num in range(1,6) if num % 2 == 1]
# print(result) """


# # 함수

# def many(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result

# print(many(1,2,3,4,5,6,7,8,9,10))

# def kwarg(**kwagrs):
#     print(kwagrs)
# kwarg(a=1, b='dic')


# a = [1,2,3]
# b = ['a','b','c']
# c = a,b
# print(c)

# mystring = " i  love you "
# mystring = mystring.split()
# print(mystring)

# for i in range(10,3,-1):
#     print(i)


# def solution(my_string, n):
    
#     item  = [my_string[i] for i in range(n)]
    
#     return ''.join(item)

# print(solution("abcdefg", 4))


# mystring = "oxooxoxxox"
# print(mystring.split('x'))
# result = mystring.split('x')
# print(result)
# # for i in range(len(result)):
# #     item = len(result[i])
# #     print(item)

# item = [len(result[i]) for i in range(len(result))]
# print(item)

# a = [293, 1000, 395, 678, 94]
# d = [94, 777, 104, 1000, 1, 12]

# def solution(arr, delete_list):

#     return [i for i in arr if i not in delete_list]

# print(solution(a,d))

# # a = "43 + 12"
# # b = a.split()
# # print(b)
# # print(b[0],b[1],b[2])

# print('a' < 'b')
# print([1,23] + [3,4,5])

# a = "12345"
# for i in a:
#     print(i)

# arr = [[1,2],[2,1]]
# for i,j in arr:
#     print(i,j)

# a = "ihrhbakrfpndopljhygc"
# print(a[::4])

# mystring = "axbxcxdx"
# print(mystring.split('x'))

# mystring2 = "dxccxbbbxaaaa"
# answer = mystring2.split('x')
# answer.sort()
# print(answer)


# a = [1,2,3,4,5]
# print(a[:3])    # slice는 마지막 index 포함 x
# a.append(6) 
# print(a)

# date1 = [2023, 10, 10]
# date2 = [2024, 1, 1]
# print(date1 > date2)

# myStr = "baconlettucetomato".split('abc')
# print(myStr)

# a = "12345"
# print(int(a))

# print(a[::1])
# print(bool(a.index('1')))

# queries = [[0, 3],[1, 2],[1, 4]]
# for i,j in queries:
#     print(i,j)

# a = [i for i in range(1,5)]
# print(a)

# a = ["abc", "def", "ghi"]
# answer = ''
# for i in range(len(a)):
#     if 'ef' not in a[i]:
#         answer += a[i]
# print(answer)

# a = []
# a += [1]
# # a.append(1)
# print(a)

# arr = [0] * 5
# print(arr)


# arr = [1,2,3,4,5]
# print(arr)
# # arr.append(a[0])
# # arr.append(a[0])
# # del arr[-3:]
# # arr.extend(arr[0] *((arr[0])* 3))
# # print(arr)

# # st = "AAAA1aaaa"
# # print(st)
# # c = st.split('1')
# # print(c)
# # b = c.pop()
# # print(b)

# myStr = "cabab"

# print(b)

# from collections import Counter
# st = ["a","bc","d","efg","hi"]

# print(b)



# # result = []
# # arr = [1, 2, 3, 100, 99, 98]
# # result.append(arr)

# # my_list = []
# # for num in arr:
# #     if num >= 50 and num % 2 == 0:
# #         num = num // 2
# #     elif num < 50 and num % 2 == 1:
# #         num = num*2 + 1
# #     my_list.append(num)
# # print(my_list)
# # result.append(my_list)
# # print(result)

# # answer = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)] 
# # lst = [0] * 52
# # print(answer)
# # print(lst)

# # my_string = "Programmers"
# # print(my_string[:0])
# # my_list =list(my_string)


# my = [1,2,3,4]
# print(sum(my))

# ia = "aAb1B2cC34oOp"
# print(sum([ int(i) for i in ia if i.isdecimal()]))

# print(ia.index('a'))

# n = 1234

# print(''.join(['1','2']))

# myString = "AbCdEFG"
# pat = "dE"
# print(myString.index(pat))
# print(myString[2] * 3)


# # picture = [".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."]

# # def solution(picture, k):
# #     # 1. 가로 확대
# #     result = []
# #     for i in range(len(picture)):
# #         answer = ''             # +=을 하면 0번째 행의 글자가 1번째 행이랑 합쳐지고 그 다음엔 2번째랑 합쳐지고... 하므로 한번 돌때마다 초기화
# #         for j in picture[i]:    # j는 str 형식으로 들어감.
# #             answer += j * k     # 한 행을 수행한다.
# #         # 2. 세로 확대    
# #         for m in range(k): 
# #             result.append(answer)   # 한 행을 마치면 리스트에 추가한다.
        
# #     return result

# # print(solution(picture,2))

# myStr = "cabab"
# print(myStr.rsplit('a',1))

# new_list = [1,2,3,5,4]
# # newnew = sorted(new_list)
# new_list.sort()
# print(new_list)

# answer = [[1, 2, 3], [3, 4, 5, 6]]
# print(len(answer)) # 행의 개수 2
# print(len(answer[0])) # 0행의 열의 개수 3
# print(len(answer[1])) # 1행의 열의 개수 4

# # 딕셔너리
# a = {'name': 'pey', 'phone': '0119993323'}
# print(a.keys())
# print(a.values())
# print(a.get('name'))

# my_list = []
# print(len(my_list))

# keys = ['a', 'b', 'c','a','a','d']
# value = 0
# d = dict.fromkeys(keys, value)
# print(d)  # 출력: {'a': 0, 'b': 0, 'c': 0}
# print(''.join(d)) # 출력 abcd

# num = 29183
# print(list(str(num)))


# dic = {0:'a', 1: 'b', 2:'c'}
# for i in dic.values():
#     print(i)

# print(dic.get(3,0))

# my_str = "3 + 4"
# answer = my_str.split(' ')
# print(answer)

# dic = ["sod", "eocd", "qixm", "adio", "soo"]
# for i in dic:
#     i.split()

# class Node: # 노드를 만들어내는 클래스이다.
#     def __init__(self,data,next = None):
#         self.data = data
#         self.next = next

# class NodeMgmt:
#     # 생성자에서 Node객체를 사용하였으므로 data, next 변수를 이용 가능하다. + head라는 변수도 이용 가능하다.
#     def __init__(self,data):
#         self.head = Node(data)  # NodeMgmt를 이용하는 순간 하나의 노드가 만들어 지는 것이다.

#     def add(self, data):
#         if self.head == '': # 노드가 아예 없으면 노드를 생성한다.
#             self.head = Node(data)
#         else:
#             node = self.head # node가 제일 처음의 노드라는 것을 의미한다.
#             while node.next:    # node.next 가 None이라면 while문을 빠져 나온다. 즉, 제일 마지막 노드라는 의미이다.
#                 node = node.next
#             node.next = Node(data)   # while문을 빠져 나왔으므로 제일 마지막 노드이다. node.next == None 이었는데 새로운 Node를 추가한다.

#     def desc(self): # 어떤 노드들이 들어있는지 확인할 수 있도록 하는 함수이다.
#         if self.head == '':
#             print('노드가 존재하지 않습니다. 노드를 먼저 생성해주세요') # 작성 안해도 된다. NodeMgmt라는 객체를 생성할 때 Node가 무조건 만들어진다.
#         node = self.head
#         while node:
#             print(node.data)
#             node = node.next

#     def delete(self,data):  # 1. 헤드를 제거 / 2. 중간,마지막 노드를 제거
        
#         if self.head.data == data:
#             del self.head
#         else:
#             node = self.head
#             while node.next:
#                 if node.next.data == data:
#                     temp = node.next    # 삭제할 노드가 node.next 이므로 temp에 저장해준다.
#                     node.next = node.next.next # node가 가지고 있는 node.next 주소를 node.next.next로 바꿔준다.
#                     del temp
#                     return
#                 else:
#                     node = node.next # if문을 통과하지 못한 경우 -> 아직 데이터를 찾지 못함. 다음 노드로 넘어가기 위함


# node = NodeMgmt(0)
# for i in range(2,10):
#     node.add(i)
# node.delete(5)
# node.delete(11)
# node.desc()

from fractions import Fraction
a = Fraction(1,5)
b = Fraction(3,5)
result = a+b
print(result)
print(result.numerator) 
print(result.denominator)
print(float(result))

print(ord('9'))

li = [1,3,2,5]
print(sorted(li))
dic = {76:1, 24:2}
print(dic[76])

a = 1
print(-a)