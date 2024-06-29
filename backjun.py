# 24 06 26 노베이스 영혼 갈아 넣기

# 1008
# a, b = map(int, input().split())
# print(a/b)


# # 10869
# a, b = map(int, input().split())
# 1 <= a <= 10000
# 1 <= b <= 10000
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)


# # 1271
# a,b = map(int, input().split())
# print(a//b)
# print(a%b)

# 1330
a,b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')

# 2741
a = int(input())
for i in range(1,a+1):
    print(i)