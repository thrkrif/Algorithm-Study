# # 큐

# def Enqueue(data_list,data):
#     data_list.append(data)

# def Dequeue(data_list):
#     del data_list[0]

# data = []

# Enqueue(data,3)
# Enqueue(data,1)
# Enqueue(data,2)
# print(data)
# Dequeue(data)
# print(data)

# def recursive(data):
#     if data < 0:
#         print('ended')
#     else:
#         print(data)
#         recursive(data-1)
#         print('returned', data)

# recursive(4)

# # 스택
# """
# 스택의 구조 push, pop
# 파이썬에서 pop은 구현되어 있지만 내가 직접 만들어보자.
# """

# data_list = list()

# # push 구현
# def push(data):
#     data_list.append(data)
# # pop 구현
# def pop():
#     data = data_list[-1]
#     del data_list[-1]
#     return data

# for i in range(5):
#     push(i)
# print(data_list)
# print(data_list.pop())
# print(data_list)


# # 링크드 리스트
# # 1. 하나의 노드를 만드는 클래스
# class Node:
#     def __init__(self, data, next = None):  # next에 아무런 입력값이 안들어가면 None으로 초기화 된다는 의미임.
#         self.data = data
#         self.next = next    # next를 입력 받았을 때

# class NodeMgmt:
#     def __init__(self,data):
#         self.head = Node(data)  # 가장 처음 생성된 노드를 head로 지정함. Node클래스를 쓰므로 data, next를 이용 가능함.
#                                 # 여기선 next를 입력 안했으므로 next는 None인 상태

#     def add(self, data):    # 맨 뒤에 노드 객체를 추가해주는 함수
#         if self.head == '': # head가 비었다면, 즉 아무런 노드도 없다면
#             self.head = Node(data)  # 노드를 생성한다.
#         else:
#             node = self.head
#             while node.next:
#                 node = node.next
#             node.next = Node(data)
        
#     def desc(self):
#         node = self.head
#         while node:
#             print(node.data)
#             node = node.next

#     def delete(self,data):
#         if self.head == '': # 방어코드
#             print("노드가 아예 없습니다. 노드를 생성하세요")


#         if self.head.data == data:  # 가장 처음 노드(헤드)를 삭제하는 경우
#             temp = self.head
#             self.head = self.head.next
#             del temp
#         else:   # 중간, 마지막 노드를 삭제하는 경우
#             node = self.head
#             while node.next:
#                 if node.next.data == data:
#                     temp = node.next
#                     node.next = node.next.next
#                     del temp
#                     pass
#                 else:
#                     node = node.next

















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

#     def search_node(self,data): # 특정 노드를 찾아서 출력하는 기능
#         node = self.head
#         while node:
#             if node.data == data:
#                 print("찾으시는 노드는", node.data)
#                 break
#             node = node.next


# mynode = NodeMgmt(0)
# mynode.desc()
# for i in range(1,10):
#     mynode.add(i)
# mynode.desc()
# mynode.search_node(3)


# 더블 링크드 리스트

class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head
    
    def insert_from_head(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new = node
            self.tail = new

    def search_from_head(self,data):
        if self.head == None:
            print("노드가 존재하지 않습니다. 노드를 생성해주세요.")
        node = self.head
        while node:
            if node.data == data:
                print("찾으시는 노드",node.data)
                return
            else:
                node = node.next
        print("찾으시는 노드가 없습니다.")
    
    def search_from_tail(self,data):
        if self.tail == None:
            print("노드가 존재하지 않습니다. 노드를 생성해주세요.")
        node = self.tail
        while node:
            if node.data == data:
                print("찾으시는 노드",node.data)
                return
            else:
                node = node.prev
        print("찾으시는 노드가 없습니다.")


    def desc(self): # 어떤 노드들이 들어있는지 확인할 수 있도록 하는 함수이다.
        if self.head == '':
            print('노드가 존재하지 않습니다. 노드를 먼저 생성해주세요') # 작성 안해도 된다. NodeMgmt라는 객체를 생성할 때 Node가 무조건 만들어진다.
        node = self.head
        while node:
            print(node.data)
            node = node.next

node = NodeMgmt(0)
node.desc()
for i in range(1,10):
    node.insert_from_head(i)
node.desc()
node.search_from_head(3)
node.search_from_tail(7)



# # 힙

# class Heap:
#     def __init__(self, data):
#         self.heap_array = list()
#         self.heap_array.append(None)  # root node의 index를 1로 하기 위해 0은 None으로 둔다.
#         self.heap_array.append(data)  # root node에 데이터 삽입
    
#     """
#     노드를 이동시켜야 하는지 판단하는 함수이다.
#     자식 노드가 부모 노드보다 크면 True를 return 한다.
#     """
#     def move_up(self, inserted_idx):
#         if inserted_idx <= 1:   # 아무것도 없거나, root node 1개뿐인 상황
#             return False    

#         parent_idx = inserted_idx // 2
#         if self.heap_array[parent_idx] < self.heap_array[inserted_idx]:
#             return True
#         else:
#             return False
        
#     def insert(self, data):
#         # 방어코드
#         if len(self.heap_array) == 0:
#             self.heap_array.append(None)  
#             self.heap_array.append(data)
#             return True
        
#         self.heap_array.append(data)
        
#         # 삽입된 data의 index 번호
#         inserted_idx = len(self.heap_array) - 1 # ex) 첫번째 요소에 0이 들어있으므로 -1 해줘야한다.
        
#         """
#         move_up이 True이면 부모노드와 자식노드의 위치 변경한다.
#         부모노드 > 자식노드가 될 때까지 반복한다.
#         """
#         while self.move_up(inserted_idx):
#             parent_idx = inserted_idx // 2
#             self.heap_array[parent_idx], self.heap_array[inserted_idx] = self.heap_array[inserted_idx],self.heap_array[parent_idx]
#             inserted_idx = parent_idx

#         return True

#     def move_down(self, popped_idx):
#         left_child_popped_idx = popped_idx * 2
#         right_child_popped_idx = popped_idx * 2 + 1

#         # case1 왼쪽 자식 노드도 없는 경우
#         if left_child_popped_idx >= len(self.heap_array):
#             return False
#         # case2 왼쪽 자식 노드는 있고 오른쪽 자식 노드는 없는 경우
#         elif right_child_popped_idx >= len(self.heap_array):
#             if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
#                 return True
#             else:
#                 return False
#         # case3 양쪽 자식 다 있는 경우
#         if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
#             if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
#                 return True
#             else:
#                 return False
#         else:
#             if self.heap_array[right_child_popped_idx] > self.heap_array[popped_idx]:
#                 return True
#             else:
#                 return False

#         # 힙 데이터 삭제 구현
#         # 힙에서 데이터 삭제는 보통 최댓값, 또는 최솟값을 추출하기 위함이다. 루트 노드를 꺼낸다.
#     def pop(self):
#         if len(self.heap_array) <= 1:  # 데이터가 안들어있거나 index 0번에 None만 들어있음.
#             return None

#         returned_data = self.heap_array[1]
#         self.heap_array[1] = self.heap_array[-1]
#         del self.heap_array[-1]
#         popped_idx = 1

#         while self.move_down(popped_idx):
#             left_child_popped_idx = popped_idx * 2
#             right_child_popped_idx = popped_idx * 2 + 1

#             # case1 왼쪽 노드만 있는 경우
#             if right_child_popped_idx > len(self.heap_array):
#                 if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
#                     self.heap_array[left_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx] , self.heap_array[left_child_popped_idx]
#                     popped_idx = left_child_popped_idx
#             # case2 오른쪽 노드도 있는경우
#             else:
#                 if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
#                     if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
#                         self.heap_array[left_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[left_child_popped_idx]
#                         popped_idx = left_child_popped_idx
#                 else:
#                     if self.heap_array[right_child_popped_idx] > self.heap_array[popped_idx]:
#                         self.heap_array[right_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[right_child_popped_idx]
#                         popped_idx = right_child_popped_idx 
#         return returned_data
    

# heap = Heap(15)
# heap.insert(10)
# heap.insert(8)
# heap.insert(5)
# heap.insert(4)
# heap.insert(20)
# print(heap.heap_array)
# heap.pop() # 20이 빠지고 8이 루트 노드로 들어갔다가 move_down으로 검사하면서 8을 있어야 할 자리로 갖다 놓는다.
# print(heap.heap_array)