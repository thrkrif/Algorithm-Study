import random

# # Queue FIFO

# a = list()

# def inq(data):
#     a.append(data)
    
# def dq():
#     print(a[0])
#     del a[0]

# for i in range(0,10):
#     inq(i)

# print(a)
# dq()
# dq()
# print(a)

# # stack

# a = list()
# def inq(data):
#     a.append(data)
    
# def dq():
#     print(a[-1])
#     del a[-1]

# for i in range(0,10):
#     inq(i)

# print(a)
# dq()
# dq()
# print(a)

# # Linked list

# class Node():
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next

# node1 = Node(1)
# node2 = Node(2)
# node1.next = node2

# # 전역변수, 첫번째 노드는 node1임을 나타냄
# head = node1
# # 노드에 데이터 추가하기
# def add(data):
#     # node는 node1을 가리킴
#     node = head
#     # 다음 노드(즉 node1이 다음 node를 가리키는 포인터가 존재한다면)
#     while node.next:
#         # node는 node2를 가리키게 됨. 이어서 다음 노드가 존재할 때 까지 반복
#         node = node.next
#     # 마지막 노드를 생성하고 포인터와 연결한다
#     node.next = Node(data)

# for index in range(3,10):
#     add(index)

# node = head
# while node.next:
#     # 8출력
#     print(node.data)
#     # 포인터를 9로 가져감, 9는 포인터가 없음 따라서 loop 종료
#     node = node.next
# # 9출력하기 위해 print
# print(node.data)

# 링크드 리스트 만들기

# class Node():
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next
#     def add(self, data):
#         self.data = data

# # add 함수 생성
# def add(data):
#     node = head
#     while node.next:
#         node = node.next
#     node.next = Node(data)

# node1 = Node(1)
# head = node1    # 첫번째 노드를 헤드로 정함
# for index in range(2,10):
#     add(index)

# node = head 

# # 링크드 리스트 출력하기
# while node.next:
#     print(node.data)
#     node = node.next    # 헤드를 다음 노드로 이동시킴
# print(node.data)

# # 링크드 리스트 삽입

# # ex) 1,2 사이에 1.5 삽입
# node3 = Node(1.5)
# node = head
# Search = True
# while Search:
#     if node.data == 1:
#         Search = False
#     else:
#         node = node.next    # 삽입 이전 노드까지 찾아온거임
# # 중간 삽입, 새로운 변수 설정해서 node.next 저장, swap 이랑 유사
# node_next = node.next
# node.next = node3
# node3.next = node_next

# while node.next:
#     print(node.data)
#     node = node.next    
# print(node.data)

# 클래스로 중간 삽입 구현

""" # 노드를 생성하는 클래스
class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

# 노드를 추가하고 출력하는 클래스
class NodeMgmt():
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        if self.head == '': # 일종의 방어코드, 이 클래스는 호출과 동시에 생성자가 자동으로 head를 만든다.
            self.head = Node(data)
        else:
            node = self.head    # head가 존재하면 node라는 변수에 저장
            while node.next:    # 마지막 노드까지 돌기
                node = node.next    # head를 그 다음 노드로 옮기기
            node.next = node.data   # 마지막 노드에 데이터를 삽입하기
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

linkedlist1 = NodeMgmt(0)
linkedlist1.desc() """


        


class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class NodeMgmt():
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node 
                # print("원하는 Data: %d" % data) 반환 값이 없으면 외부에서
                # 검색된 노드를 추가로 사용할 수 없다.
            node = node.next

    def delete(self, data):
        if self.head == '':
            print("삭제할 노드가 없습니다.")
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:    
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next  # 마지막 노드의 겨웅 node.next.next = None
                    del temp
                    return
                else:   
                    node = node.next


linkedList = NodeMgmt(0)

for i in range(1,10):
    linkedList.add(i)
linkedList.desc()

linkedList.delete(9)
linkedList.desc()

for i in range(0,10):
    linkedList.add(random.randint(1,9))
linkedList.desc()
node = linkedList.find(4)
print(node.data)

# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)


# 더블 링크드 리스트
class Node():   # 노드를 만드는 역할
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class NodeMgmt():   
    def __init__(self, data):   # 이 클래스를 실행 시 자동으로 노드 하나를 만든다.
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:   # 방어 코드
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)
double_linked_list.desc()


# 더블 링크드 리스트, tail에서 검색해오며 삽입
class Node():   # 노드를 만드는 역할
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class NodeMgmt():   
    def __init__(self, data):   # 이 클래스를 실행 시 자동으로 노드 하나를 만든다.
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:   # 방어 코드
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def search_from_head(self, data):
        if self.head == None:
            return False
        else:
            node = self.head
            while node:
                if node.data == data:
                    return node
                else:
                    node = node.next
            return False
    
    def search_from_tail(self, data):
        if self.head == None:
            return False
        else:
            node = self.tail
            while node:
                if node.data == data:
                    return node
                else:
                    node = node.prev
            return False
        
    def insert_before(self, data, before_data): # data가 삽입 하려는 것임
        if self.head == None:
            self.head = Node(data)
            return True     # head가 없으면 head를 만들고 그것이 삽입한 데이터이다.
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev  # 기존 노드, 앞에 있던 노드를 사용하려고 변수 생성한거임
            before_new.next = new
            new.prev = before_new
            new.next = node # node, node.prev 차이가 뭐임? 안겹치고 양쪽에서 사용하려고 이름만 다르게 한건가?
            node.prev = new
            return True
    def insert_after(self, data, after_data):
        if self.head == None:
            self.head = Node(data)
            return True     # head가 없으면 head를 만들고 그것이 삽입한 데이터이다.
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node == None:
                    return False
            new = Node(data)
            after_new = node.next    # 뒤에 노드를 사용하려고 변수 만든거임
            node.next = new
            new.prev = node
            new.next = after_new
            after_new.prev = new
            return True

node_mgmt = NodeMgmt(0)
for data in range(1, 10):
    node_mgmt.insert(data)

node_mgmt.desc()
node_mgmt.insert_before(3.5,4)
node_mgmt.insert_after(1.5, 1)
node_mgmt.desc()


# Hash

hash_table = list([i for i in range(10)])
print(hash_table)

# hash 주소를 추출 하는 연산
def hash_func(key):
    return key % 5

data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
data4 = 'Anthor'
## ord(): 문자의 ASCII(아스키)코드 리턴
print (ord(data1[0]), ord(data2[0]), ord(data3[0]))
print (ord(data1[0]), hash_func(ord(data1[0])))
print (ord(data1[0]), ord(data4[0]))

def storage_data(data, value):
    key = ord(data[0])  # key를 추출하는 연산
    hash_address = hash_func(key)   # 키를 해시 함수 연산하여 해시 주소를 추출
    hash_table[hash_address] = value    # 해시 테이블[해시 주소] -> 슬롯에 데이터(value) 저장

storage_data('Andy', '010-2345-6081')
storage_data('Dave', '010-2222-6081')
storage_data('Trump', '010-3333-6081')

def get_data(data):
    key = ord(data[0])  
    hash_address = hash_func(key)   
    return hash_table[hash_address]

print(get_data('Andy'))



# 직접 해시를 만들어보자

data1 = 'kim'
data2 = 'lee'
data3 = 'yang'

def hash_func(key):
    return key % 5
    
def get_storage(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

get_storage(data1, '11')
get_storage(data2, '22')
get_storage(data3, '33')

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data(data1))
print(get_data('lee'))



# 2024/06/30 해시 복습
# 연습1: 리스트 변수를 활용해서 해쉬 테이블 구현해보기
# 1. 해쉬 함수: key % 8
# 2. 해쉬 키 생성: hash(data)

data1 = 'a'
data2 = 'b'
data3 = 'c'


def hash_func1(key):
    return key % 8

def storage(data, value):
    key = ord(data[0])
    hash_address = hash_func1(key)
    hash_table[hash_address] = value

def get_value(data):
    key = ord(data[0])
    hash_address = hash_func1(key)
    return hash_table[hash_address]



storage('a',213)
storage('Hello', 'World')

print(get_value('a'))
print(get_value('Hello'))    

import hashlib

data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(b'test')
hex_dig = hash_object.hexdigest()
print(hex_dig)  # test라는 값에 sha1이라는 해시 함수를 통해 나온 hash값이 16진수로 변환한(hexdigest()) 이와 같다.

# sha1 보다 더 보안 잘 되어있는게 sha256




# 트리

# 이진 탐색 트리

class Node:
    def __init__(self, value):   # leaf node일 수 있으므로 생성과 동시에 left, right를 만들지는 않는다.
        self.value = value
        self.left = None    # 왼쪽 브랜치
        self.right = None   # 오른쪽 브랜치

class NodeMgmt:
    def __init__(self,head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head

        while True:
            if value < self.current_node.value :   # 왼쪽 노드에 데이터를 추가
                if self.current_node.left != None:
                    self.current_node = self.current_node.left     # left에 자식 노드가 있다는 것을 의미
                else:
                    self.current_node.left = Node(value)    # 데이터가 없으면 데이터를 추가하고 실행을 마친다.
                    break
            else:   # 오른쪽 노드에 데이터를 추가(value > self.current_node 인 경우)
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self,value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

         # 삭제할 node 탐색
    def delete(self,value):
        searched = False
        self.parent = self.head
        self.current_node = self.head

        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if searched == False:
            return False
        
        # 위 delete로 이미 삭제할 node가 self.current_node가 되었음

        # case1 삭제할 node가 leaf node인 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node

        # case2 삭제할 node의 child가 하나 있는 경우 -> 1) left child 2) right child
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # case3 삭제할 node의 childe가 2개인 경우
        # 1.왼쪽 node의 가장 큰 값으로 대체
        # 2.오른쪽 node의 가장 작은 값으로 대체 -> 코드를 2번으로 만들겠음
        # 2-1. 가장 작은 값에 child가 없음, 2-2. 가장 작은 값에 오른쪽 child가 존재함

        # child가 두 개임을 의미
        if self.current_node.left != None and self.current_node.right != None:
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.rigth
            # value > self.parent.value 인 경우
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(5)

print(BST.search(4))



# Heap

class Heap:
    def __init__(self,data):
        # 배열을 만들어주고 index가 1부터 시작하도록 index 0에는 None을 집어 넣어준다.
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self,inserted_idx):
        # 삽입한 데이터의 index가 1보다 작거나 같으면 데이터가 없거나 root node라는 뜻이므로 move_up 할 필요가 없다.
        if inserted_idx <= 1:
            return False
        # 자식 > 부모이면 move_up 한다.
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self,data):
        # 방어코드로 힙에 아무것도 들어가있지 않은 경우 data를 추가해준다.
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)

         # 추가되는 데이터는 제일 마지막에 들어오게 된다.
        inserted_idx = len(self.heap_array) - 1

        # 자식 > 부모인 경우 계속 move_up은 True를 반환한다, while문 내에서는 부모와 자식의 데이터를 swap한다.
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        return True

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        # 자식이 없을 때
        if left_child_popped_idx >= len(self.heap_array):
            return False
        
        # 왼쪽 노드에 자식 있을 때
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
        # 자식이 두명 있을 때
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[right_child_popped_idx] > self.heap_array[popped_idx]:
                    return True
                else:
                    return False
            
    def pop(self):
        if len(self.heap_array) <= 1:
            return None
        # 데이터 덮어쓰기 하므로 별도로 삭제할 필요가 없다.
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # 왼쪽 노드에 자식 있을 때
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx],self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
                        self.heap_array[popped_idx],self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_popped_idx
                else:
                    if self.heap_array[right_child_popped_idx] > self.heap_array[popped_idx]:
                        self.heap_array[popped_idx],self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = right_child_popped_idx
        return returned_data

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
heap.pop()
print(heap.heap_array)
heap.pop()
print(heap.heap_array)
heap.pop()
print(heap.heap_array)


# 버블 정렬

def bubblesort(data):
    for index in range(len(data) - 1): 
        swap = False   
        for index2 in range(len(data) - index -  1): 
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1],data[index2] 
                swap = True
        if swap == False:
            break
    return data

import random

data_list = random.sample(range(100),10)
print(bubblesort(data_list))


# 삽입 정렬

def insertion_sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2],data[index2 - 1] = data[index2 - 1],data[index2]
            else:
                break

    return data
data_list = random.sample(range(100),10)
print(insertion_sort(data_list))

# 선택 정렬

def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
            data[lowest],data[stand] = data[stand],data[lowest]
    return data

data_list = random.sample(range(100),10)
print(selection_sort(data_list))


# 재귀

def fac(n):
    if n > 1:
        return n * fac(n-1)
    else:
        return n

print(fac(1))
print(fac(5))

def sum_list(data):
    if len(data) == 1:
        return data[0]
    else:
        return data[0] + sum_list(data[1:])

data = [1,2,3,4,5,6,7,8,9,10]
print(sum_list(data))

for index in range(int(2.5)):
    print(index)

def func(n):
    print(n)
    if n == 1:
        return n
    if n % 2 == 1:
        return func((3 * n) + 1)
    else:
        return func(int(n / 2))
print(func(3))

# recursive call을 이용한 피보나치, 스택에 중복된 데이터가 쌓인다.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

""" dp = [0] * 101
dp[1],dp[2],dp[3],dp[4],dp[5] = 1,1,1,2,2
for index in range(6,101):
    dp[index] = dp[index-1] + dp[index-5]

print(dp[10])
print(dp[6])
print(dp[12]) """


# split recursive?
# 리스트를 재귀 호출을 이용하여 단일 원소가 될 때까지 나누어 보자
def split(data):
    if len(data) <= 1:
        return data
    
    medium = int(len(data) / 2)
    left = split(data[:medium])
    right = split(data[medium:])

    return left + right

data_list = [10,6,7,1,3,9]
print(split(data_list))

print(5//2)

# 퀵 정렬

# 다음 리스트를 리스트 슬라이싱(예 [:2])을 이용해서 세 개로 짤라서 각 리스트 변수에 넣고 출력해보기
data_list = [1,2,3,4,5]
data1 = data_list[:2]
data2 = data_list[2:3]
data3 = data_list[3:]
print(data1)
print(data2)
print(data3)

# 다음 리스트를 맨 앞에 데이터를 기준으로 작은 데이터는 left 변수에, 그렇지 않은 데이터는 right 변수에 넣기
data_list = [4,1,2,5,7]
pivot = data_list[0]
left,right = list(),list()
for index in data_list:
    if index < pivot:
        left.append(index)
    elif index > pivot:
        right.append(index)
    else:
        False    
print(left)
print(right)

# data_list 가 임의 길이일 때 리스트를 맨 앞에 데이터를 기준으로 작은 데이터는 left 변수에, 그렇지 않은 데이터는 right 변수에 넣기
def example(data_list):
    
    if len(data_list) <= 1:
        return data_list
    
    pivot = data_list[0]
    left,right = list(),list()

  
    for index in data_list[1:]:
        if index < pivot:
            left.append(index)
        else:
            right.append(index)
    
    
    return example(left) + [pivot] + example(right)

import random
data = random.sample(range(100),10)
print(example(data))

# 퀵 정렬 list comprehension 으로 만들어 보기

def qsort_list(data_list):
    if len(data_list) <= 1:
        return data_list
    
    pivot = data_list[0]
    left = [item for item in data_list[1:] if pivot > item]
    right = [item for item in data_list[1:] if pivot <= item]

    return qsort_list(left) + [pivot] + qsort_list(right)

import random
data = random.sample(range(100),10)
print(qsort_list(data))


# binary search
def binary_search(data,search):
    print(data)
    if len(data) == 1:
        if data[0] == search:
            return 1
        else:
            return 0
    if len(data) == 0:
        return 0
    medium = len(data) // 2
    if data[medium] == search:
        return 1
    else:
        if data[medium] > search:
            return binary_search(data[:medium],search)
        else:
            return binary_search(data[medium+1:],search)

import random
data = random.sample(range(100),10)
print(data)
data.sort()
print(data)

binary_search(data,86)

# 백트랙킹

def is_available(current_candidate, current_col):
    current_row = len(current_candidate)
    for queen_row in range(current_row):
        if current_candidate[queen_row] == current_col or abs(current_candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        return
    
    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col) # 퀸의 위치를 저장
            DFS(N, current_row + 1, current_candidate, final_result)
            current_candidate.pop() # 여기로 넘어왔단 것은 위의 DFS가 실행이 안되었음을 의미한다.
            # 백트랙킹을 한다.


def Nqueens(N):
    final_result = []
    DFS(N,0,[],final_result)
    return final_result

print(Nqueens(4))