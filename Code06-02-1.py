## 함수
def isStackFull():
    global SIZE, stack, top
    if (top == SIZE-1):
        return True
    else:
        return False

def isStackEmpty():
    global SIZE,stack,top
    if(top<=-1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack,top
    if isStackFull():
        print('스택 꽉 찼음')
        return
    top+=1
    stack[top]=data
    return

def pop():
    global SIZE,stack,top
    if isStackEmpty():
        print('스택 비었음')
        return None
    data=stack[top]
    stack[top]=None
    top-=1
    return data

def peek(): # pop하기 전 pop하면 나올 데이터 확인
    global SIZE,stack,top
    if isStackEmpty():
        print('스택 비었음')
        return None
    return stack[top]


## 변수
SIZE=5  # 상수
stack=[None for _ in range(SIZE)]# 오버플로우(넘치다) 주의!
top=-1

## 메인
print('바닥',stack)
push('커피')
push('녹차')
# push('꿀물')
# push('콜라')
# push('환타')
# print('바닥',stack)
# push('게토레이')
print('바닥',stack)

returnData=pop()
print('pop---> ',returnData)
print('다음예정 ==>',peek())
returnData=pop()
print('pop---> ',returnData)
returnData=pop()
print('바닥',stack)
print('pop---> ',returnData)
