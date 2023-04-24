## 함수
class Node():
    def __init__(self):
        self.data=None
        self.link = None

def printNode(start):
    current = start
    print(current.data, end=" ")
    while (current.link != None):
        current = current.link
        print(current.data, end=" ")
    print()


def insertNode(findData, insertData):
    global memory,head, current, pre
    #case1 : head앞에 삽입(다현, 화사)
    if (head.data==findData):
        node=Node()
        node.data=insertData
        node.link=head
        head=node
        memory.append(node)
        return
    #case2 : 중간 노드의 삽입(사나,솔라)
    current=head
    while(current.link!=None):
        pre=current
        current=current.link
        if current.data==findData:
            node=Node()
            node.data=insertData
            node.link=current
            pre.link=node
            memory.append(node)
            return
    # case3 : 없는 노드 앞에 삽입 == 마지막노드에 추가 ( 재남, 문별 )
    node=Node()
    node.data=insertData
    current.link=node
    memory.append(node)
    return

def deleteNode(deletedata):
    global head, pre, current, memory
    # case1 : head를 삭제하는 경우(다현)
    if deletedata==head.data:
        current=head
        head=head.link
        del(current)
        return
    #case2: 중간에 삭제하는 경우(쯔위)
    current=head
    while current.link!=None:
        pre=current
        current=current.link
        if (current.data==deletedata):
            pre.link=current.link
            del(current)
            return
    # case3: 없는 노드 삭제
    return

def findNode(findData):
    global head, pre, current, memory
    current=head
    if current.data==findData:
        return current
    while current.link!=None:
        current=current.link
        if current.data==findData:
            return current
    return Node()


## 변수
memory=[]
head, current, pre= None, None, None
dataArray=['다현','정연','쯔위','사나','지효']

## 메인
node=Node() # 첫노드
node.data=dataArray[0]
head=node
memory.append(node)

for data in dataArray[1:]:
    pre=node
    node=Node()
    node.data=data
    pre.link=node
    memory.append(node)

# 데이터 출력
printNode(head)

# 데이터 삽입
# insertNode('다현','화사') # head에 삽입하는 경우
# printNode(head)

insertNode('사나','솔라')# 중간에 삽입하는 경우
printNode(head)

insertNode('재남','솔라')# 없는 노드에 삽입하는 경우
printNode(head)

deleteNode('다현') # head에 있는 노드 삭제
printNode(head)

deleteNode('쯔위') # 중간에 있는 노드 삭제
printNode(head)

deleteNode('재남') # 없는 노드 삭제
printNode(head)

returnData=findNode('사나')
print(returnData.data,'뮤비가 나옵니다.')

returnData=findNode('재남')
print(returnData.data,'뮤비가 나옵니다.')