## 함수
def add_data(friend):
    katok.append(None) # 빈칸 추가
    klen=len(katok)
    katok[klen-1]=friend # 추가

def insert_data(position,friend):
    katok.append(None)  # 빈칸 추가
    klen=len(katok)
    for i in range(klen-1,position,-1): # 오른쪽으로 땡기기
        katok[i]=katok[i-1]
        katok[i-1]=None
    katok[position]=friend # 자리에 추가

def delete_data(position):
    katok[position]=None # 삭제
    klen=len(katok)
    for i in range(position+1,klen):# 왼쪽으로 떙기기
        katok[i-1]=katok[i]
        katok[i]=None
    del(katok[klen-1]) # 빈칸제거

## 전역
katok=[]

## 메인
# 데이터 추가
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)
# 데이터 삽입
insert_data(3,'미나')
print(katok)
# 데이터 삭제
delete_data(4)
print(katok)
