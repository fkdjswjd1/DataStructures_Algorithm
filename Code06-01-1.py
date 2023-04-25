# 스택

## 함수


## 변수
stack=[None,None,None,None,None]
top=-1

## 메인
# Push
top+=1
stack[top]='커피'

top+=1
stack[top]='녹차'

print('바닥',stack)

# Pop
data=stack[top]
stack[top]=None
top-=1
print('pop---> ',data)

data=stack[top]
stack[top]=None
top-=1
print('pop---> ',data)

print('바닥',stack)