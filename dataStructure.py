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
heap = Heap(1)
print(heap.heap_array)
        














