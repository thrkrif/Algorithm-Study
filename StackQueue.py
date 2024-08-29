# # 24/06/23

# """ # 큐를 구현해보자 FIFO Queue
# a = list()
# while True:
#     print('''
#     1.Enqueue
#     2.Dequeue
#     3.Quit    
#       ''')
#     user = int(input())
#     if user == 1:
#         a.append(input())
#         print('Queue is filled')
#         print(a)
#     elif user == 2:
#         if len(a) == 0:
#             print('Queue is empty')
#             continue
#         else:
#             print("get: ",a.pop(0))
#     elif user == 3:
#         print("Quit")
#         print("Current Queue State", a)
#         break
#     else:
#         break """


# """ # 비어 있는 리스트 생성 / LIFO Queue이다 Stack이랑 같은 구조
# a = list()
# while True:
#     print('''
#     1.Enqueue
#     2.Dequeue
#     3.Quit    
#       ''')
#     user = int(input())
#     if user == 1:
#         a.append(input())
#         print('Queue is filled')
#         print(a)
#     elif user == 2:
#         if len(a) == 0:
#             print('Queue is empty')
#             continue
#         else:
#             print("pop: ",a.pop())
#     elif user == 3:
#         print("Quit")
#         print("Current Queue State", a)
#         break
#     else:
#         break
#  """

# import queue
# # 리스트 변수로 Queue 구현해보기

# a = list()

# def enqueue(data):
#     a.append(data)

# def dequeue():
#     data = a[0]
#     del a[0]
#     return data

# for index in range(10):
#     enqueue(index)

# print(len(a))
# print(dequeue())
# print(dequeue())
# print(dequeue())

# # 스택 구현 -> FILO, LIFO
# # 프로세스 구현하는 함수에 자주 사용 된다. ex) 재귀함수

# a = list()

# def push(data):
#     a.append(data)

# def pop():
#     data = a[-1]
#     del a[-1]
#     return print(data)

# for i in range(0,10):
#     push(i)
# print(a)

# pop()
# pop()

# class Quadrangle:
#     width = 0
#     height = 0
#     color = 'black'

#     def set_all(self, width, height, color):
#         self.width = width
#         self.height = height
#         self.color = color
    
#     def get_area(self):
#         return print(self.width * self.height)
    
#     def get_color(self):
#         return print(self.color)
    
# square1 = Quadrangle()
# square2 = Quadrangle()
# square1.set_all(10,5,'red')
# square2.set_all(7,7,'blue')

# square1.get_area()
# square1.get_color()

# square2.get_area()
# square2.get_color()


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data) 

node1 = Node(1)
head = node1
for index in range(2, 10):
    add(index)

while node1.next:
    print(node1.data)
    node1 = node1.next
print(node1.data)   # 마지막 노드



