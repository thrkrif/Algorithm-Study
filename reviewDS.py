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