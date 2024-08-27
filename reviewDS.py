# 큐

def Enqueue(data_list,data):
    data_list.append(data)

def Dequeue(data_list):
    del data_list[0]

data = []

Enqueue(data,3)
Enqueue(data,1)
Enqueue(data,2)
print(data)
Dequeue(data)
print(data)

def recursive(data):
    if data < 0:
        print('ended')
    else:
        print(data)
        recursive(data-1)
        print('returned', data)

recursive(4)

# 스택
"""
스택의 구조 push, pop
파이썬에서 pop은 구현되어 있지만 내가 직접 만들어보자.
"""

data_list = list()

# push 구현
def push(data):
    data_list.append(data)
# pop 구현
def pop():
    data = data_list[-1]
    del data_list[-1]
    return data

for i in range(5):
    push(i)
print(data_list)
print(data_list.pop())
print(data_list)


# 링크드 리스트
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
    def add(self, data):
        node = head
        while node.next:
            node = node.next
        node.next = Node(data)


node1 = Node(1)
head = node1
for index in range(2,10):
    node1.add(index)

node = head
while node.next:
    print(node.data)
    node = node.next
print (node.data)

# 힙

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)  # root node의 index를 1로 하기 위해 0은 None으로 둔다.
        self.heap_array.append(data)  # root node에 데이터 삽입
    
    """
    노드를 이동시켜야 하는지 판단하는 함수이다.
    자식 노드가 부모 노드보다 크면 True를 return 한다.
    """
    def move_up(self, inserted_idx):
        if inserted_idx <= 1:   # 아무것도 없거나, root node 1개뿐인 상황
            return False    

        parent_idx = inserted_idx // 2
        if self.heap_array[parent_idx] < self.heap_array[inserted_idx]:
            return True
        else:
            return False
        
    def insert(self, data):
        # 방어코드
        if len(self.heap_array) == 0:
            self.heap_array.append(None)  
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)
        
        # 삽입된 data의 index 번호
        inserted_idx = len(self.heap_array) - 1 # ex) 첫번째 요소에 0이 들어있으므로 -1 해줘야한다.
        
        """
        move_up이 True이면 부모노드와 자식노드의 위치 변경한다.
        부모노드 > 자식노드가 될 때까지 반복한다.
        """
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[parent_idx], self.heap_array[inserted_idx] = self.heap_array[inserted_idx],self.heap_array[parent_idx]
            inserted_idx = parent_idx

        return True

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        # case1 왼쪽 자식 노드도 없는 경우
        if left_child_popped_idx >= len(self.heap_array):
            return False
        # case2 왼쪽 자식 노드는 있고 오른쪽 자식 노드는 없는 경우
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
                return True
            else:
                return False
        # case3 양쪽 자식 다 있는 경우
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

        # 힙 데이터 삭제 구현
        # 힙에서 데이터 삭제는 보통 최댓값, 또는 최솟값을 추출하기 위함이다. 루트 노드를 꺼낸다.
    def pop(self):
        if len(self.heap_array) <= 1:  # 데이터가 안들어있거나 index 0번에 None만 들어있음.
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # case1 왼쪽 노드만 있는 경우
            if right_child_popped_idx > len(self.heap_array):
                if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
                    self.heap_array[left_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx] , self.heap_array[left_child_popped_idx]
                    popped_idx = left_child_popped_idx
            # case2 오른쪽 노드도 있는경우
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
                        self.heap_array[left_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[left_child_popped_idx]
                        popped_idx = left_child_popped_idx
                else:
                    if self.heap_array[right_child_popped_idx] > self.heap_array[popped_idx]:
                        self.heap_array[right_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[right_child_popped_idx]
                        popped_idx = right_child_popped_idx 
        return returned_data
    

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
heap.pop() # 20이 빠지고 8이 루트 노드로 들어갔다가 move_down으로 검사하면서 8을 있어야 할 자리로 갖다 놓는다.
print(heap.heap_array)