""" # 이진 탐색 트리 구현

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
                
head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(5)

print(BST.search(4))
print(BST.search(5)) 
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
 """

# 버블 정렬 직접 짜보기
# 1. 앞,뒤 데이터 비교
# 2. 바깥 로직 한번 돌 때 마다 맨 뒤 숫자가 정해짐
# 3. 이미 정렬이 되어 있다면 더 이상 반복할 필요가 없으므로 반복 횟수를 줄여야 할 필요가 있음

# data는 list가 들어갈 것임
def bubblesort(data):
        # 바깥 로직은 위에 말한 2번이 한 번 수행되었다는 것을 의미함.
        for index in range(len(data)-1):
            swap = False # 3번 조건을 충족 시키기 위해 swap = True이면 정렬이 되어 있다는 의미임
            # -index를 하는 이유도 마찬가지로 3번 조건, 바깥 로직이 한 번 돌때마다 맨 뒤에 숫자는 이미 정해지므로 비교할 필요가 없음
            for index2 in range(len(data) - index - 1):
                if data[index2] > data[index2 + 1]:
                    # swap
                    data[index2],data[index2 + 1] = data[index2 + 1],data[index2]
                    swap = True
            # 안쪽 반복문을 돌았는데도 False가 나온다면 리스트가 이미 정렬 되어있다는 것을 의미함 따라서 반복문을 빠져나옴.
            if swap == False:
                break
        # return 값을 반환함
        return data

import random
data_list = random.sample(range(100), 20)
print(bubblesort(data_list))

# recursive call

def factorial(n):
     if n <= 1:
          return 1
     else:
          return n * factorial(n-1)

print(factorial(5))

# 숫자가 들어 있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만드세요

def sum_list(data):
    if len(data) <= 1:
        return data[0]
    else:
        return data[0] + sum_list(data[1:])
data_list = [item for item in range(1,11)]
print(sum_list(data_list))

# 회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함
# 회문을 판별할 수 있는 함수를 재귀함수를 활용해서 만들어봅니다.

def palindrome(string):
     if len(string) <= 1:
          return True
     
     if string[0] == string[-1]:
          return palindrome(string[1:-1])
     else:
          return False

print(palindrome("level"))
print(palindrome("levol"))
print(palindrome("ll"))

""" 1, 정수 n에 대해
2. n이 홀수이면 3 X n + 1 을 하고,
3. n이 짝수이면 n 을 2로 나눕니다.
4. 이렇게 계속 진행해서 n 이 결국 1이 될 때까지 2와 3의 과정을 반복합니다. """

# 콜라츠 추측

def recursive(n):
    print(n)
    if n == 1:
        return n
    if n % 2 == 1:
         return recursive((3 * n) + 1)
    elif n % 2 == 0:
         return recursive(int(n / 2))

print(recursive(30))

def recursive2(n):
    if n == 1:
         return 1
    elif n == 2:
         return 2
    elif n == 3:
         return 4
    
    return recursive2(n-1) + recursive2(n-2) + recursive2(n-3)

print(recursive2(5))

# recursive2를 Dynamic Programming 으로 표현하면?

dp = [0] * 101
dp[1],dp[2],dp[3] = 1,2,4
for index in range(4,101):
     dp[index] = dp[index-1] + dp[index-2] + dp[index-3]

print(dp[5])

# DP

# recursive를 이용하는 경우 시간이 오래걸린다. 왜냐면 실행할 때마다 이전의 값들을 다시 구해야함.
def fibo(n):
     if n == 0:
          return 0
     elif n == 1:
          return 1
     return fibo(n-1) + fibo(n-2)

print(fibo(10))

# 따라서 이전의 값들을 이용하는 문제는 DP로 푸는게 효율적임.

def DpFibo(num):
     cache = [0 for index in range(num+1)]
     cache[1] = 1
     for index in range(2, num+1):
          cache[index] = cache[index-1] + cache[index-2]
     return cache[num]

print(DpFibo(10))

# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

""" n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for index in range(3,1001):
     dp[index] = dp[index-1] + dp[index-2]

print(dp[n] % 10007) """

# merge sort

# 어떤 데이터리스트가 있을 때 리스트를 앞뒤로 짜르는 코드 작성해보기 (일반화)
def split(data_list):
     medium = len(data_list) // 2
     left = data_list[:medium]
     right = data_list[medium:]
     print(left,right)

data_list = [1,2,3,4,5]
split(data_list)

# 다음 문장을 코드로 작성해보기 (merge함수는 아직은 없는 상태, 있다고만 가정)
# * mergesplit 함수 만들기
#   - 만약 리스트 갯수가 한개이면 해당 값 리턴
#   - 그렇지 않으면, 리스트를 앞뒤, 두 개로 나누기
#   - left = mergesplit(앞)
#   - right = mergesplit(뒤)
#   - merge(left, right)

def mergeSplit(data_list):
     if len(data_list) <= 1:
          return data_list

     medium = len(data_list) // 2
     left = mergeSplit(data_list[:medium])
     right = mergeSplit(data_list[medium:])
     
     return merge(left, right)

def merge(left,right):
    merged = list()
    left_point, right_point = 0,0

    # left/right 둘 다 있을 때
    while len(left) > left_point and len(right) > right_point:
            if left[left_point] > right[right_point]:
                merged.append(right[right_point])
                right_point += 1
            else:
                merged.append(left[left_point])
                left_point += 1
    # case2 - left 데이터만 남아있을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1
        
    # case3 - right 데이터만 남아있을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged

import random
data_list = random.sample(range(100),10)
print(data_list)
print(mergeSplit(data_list))

# binary search



# 순차 탐색

def search(data_list,search):
     index = 0
     while len(data_list):
          if data_list[index] == search:
            return index
          else:
               index += 1

data_list = [1,5,6,3,2]
print(search(data_list, 2))