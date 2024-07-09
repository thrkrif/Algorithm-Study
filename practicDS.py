# 이진 탐색 트리 구현

class Node:
    def __init__(self,value):
        self.value = value
        # 처음 노드를 만들때는 브랜치가 없음
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self,head):
        self.head = head
    
    def insert(self,value):
        self.current_node = self.head
        
        while True:
            if value < self.current_node.value: #   데이터가 왼쪽으로 가는 경우
                if self.current_node.left != None:  #   왼쪽 브랜치에 데이터가 있으면 현재 노드를 이동 시킨다.
                    self.current_node = self.current_node.left
                else:   #   왼쪽 브랜치에 데이터가 없으면 노드를 생성하고 while문에서 빠져 나온다.
                    self.current_node.left = Node(value)
                    break
            else: # value > self.current_node.value 인 경우
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self,value):
        self.current_node = self.head
        # node가 존재하는 경우 계속하여 순회하겠음
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        # while문을 다 돌았는데도 value를 찾지 못하였다면 False를 return 함.
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
                
""" head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(5)

print(BST.search(4))
print(BST.search(5)) """

import random
# 중복을 없애기 위해 집합으로 생성
bst_nums = set()
# 0~999 난수를 100개 생성할 것임
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0,999))
print(bst_nums)

# 아무것도 뜨지 않으면 트리가 정상 실행되었음을 의미함.
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

for num in bst_nums:
    if binary_tree.search(num) == False:
        print('searched Failed', num)

delete_nums = set()
# 집합은 indexing 지원 안하므로 list로 변경한다,
bst_nums =  list(bst_nums)
while len(delete_nums) != 10:
    # bst_nums의 인덱스를 무작위로 10개 뽑는다.
    delete_nums.add(bst_nums[random.randint(0,99)])

for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete Failed', del_num)



