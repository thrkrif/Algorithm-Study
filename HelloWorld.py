# 2024/06/20

a = 7
b = 3
print(a+b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)

food = "Python's favorite food is perl"
print(food)

food = '"Pythons favorite food is perl"'
print(food)

food = '"Python\'s favorite food is perl"'
print(food)

#줄바꿈도 문자 길이에 포함
multiline  = "Life is too short\nYou need python"
print(multiline)
print(len(multiline))

# ''' 는 맨 앞,뒤에도 \n 이 있음
multiline = '''
Life is too short
You need Python
'''
print(multiline)
print(len(multiline))

a =  'You need python'
print(len(a))

# indexing , slicing

print(a[0])
b = a[4] + a[5]*2 + a[7]
print(b)

a = '20240620Sunny'
year  = a[:4]
month = a[4:6]
day = a[6:8]
weather = a[8:]
print(year +' '+ month + ' ' + day + ' ' + weather)

# fommating

a = "현재 온도는 %d도 입니다." % 25
print(a)

# formating upgrade 

a = "현재 온도는 {0}도 입니다." .format(27)
print(a)

number = 20
month = "June"
day = "Thu"
a = "오늘은 2024년 {0} {1}일 {2}입니다." .format(month, number, day)
print(a)

a = "내일은 2024년 {0} {number}일 {day:0.4f}입니다." .format(month, number = 21, day = 3.141589)
print(a)

a = "{0:^10}" .format("hi")
print(a)

a = "{0:=^10}" .format("hi")
print(a)

# 자동으로 반올림됨, 63 line에서도 마찬가지로 반올림 된다.
y = 3.123456
a = "{0:0.4f}" .format(y)
print(a)

a = "{number:10.4f}" .format(number=3.14527592)
print(a)
a = "{number:<10.4f}" .format(number=3.14527592)
print(a)

a = "{Hello}" .format(Hello = "name")
print(a)
a = "{{Hello}}" .format()
print(a)
# 결과 : Hello 그대로 나온다.
a = "{{Hello}}" .format(Hello = "name")
print(a)

# f 문자열 포매팅
name  ="Yang"
age = 27
a = f'내 이름은 {name}, 나는 내년이면 {age+1}살이 된다.'
print(a)

d = {'name':'Yang', 'age' : 27}
a = f'내 이름은 {d["name"]}, 나는 내년이면 {d["age"] + 1}살이 된다.'
print(a)

a = f'{{and}}'
print(a)
a = f'{"python":!^12}'
print(a)
a = "{0:!^12}" .format("python")
print(a)

# 문자열 관련 함수
# count
a = "bobby"
print(a.count('b'))

# find, index
print(a.find('c'))
print(a.find('b'))
print(a.index('o'))

# join
a = ",".join('abcd')
print(a)

# lstrip, rstrip, strip
a = " Hi "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

# split
a = " a, b, c, d "
print(a.split())
print(a.split(','))

# List Type
a = [1,2,3,4,5]
print(a[1:3])

# append
a = [1,2,3,4]
a.append(5)
print(a)

# sort
a = [1,3,5,2]
a.sort()
print(a)

# reverse
a.reverse()
print(a)

# insert(index, value)
a.insert(4,4)
print(a)
a.sort()
print(a)

# del, remove, pop
# del은 인덱스를 이용하여 요소를 제거
# remove는 요소를 이용하여 요소 제거
# pop() 은 맨 마지막 요소 제거, pop(index)

# count(value)
a = [1,1,1,2,3,4,4,5]
b = a.count(1)
print(b)

# extend --> extra List
a.extend([6,7])
print(a)

# tuple 요소 수정, 삭제 불가하다. 외에 리스트와 거의 비슷하다.
t = 1,2,3
print(t+(4,))

# dictionary
a = {1:'a'}
a[2] = 'b'
print(a)
a[3] = [1,2,3]
a['name'] = 'pey'
print(a)
del a[1]
print(a)

b = a['name']
print(b)

# dictionary 관련 함수

# keys(), values()
b = a.keys()
print(b)
b = a.values()
print(b)

for k in a.keys():
    print(k)

# items() -> 전체는 리스트, 속성은 튜플
b = a.items()
print(b)
print(list(b))

# 2024 06 21

