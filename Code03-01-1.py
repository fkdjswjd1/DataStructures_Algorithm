## 함수 선언부


## 전역 변수부
katok=['다현','정연','쯔위','사나','지효']

## 메인 코드부
print(katok)

# 데이터 추가: 모모한테 카톡 1회
katok.append(None) # 빈칸 추가
katok[5]='모모'
print(katok)

# 데이터 삽입 : 미나한테 카톡 40회 (3등으로 삽입)
katok.append(None) # 빈칸 추가
katok[6]=katok[5] # 복사
katok[5]=None  # 제거
katok[5]=katok[4] # 복사
katok[4]=None  # 제거
katok[4]=katok[3] # 복사
katok[3]=None  # 제거
katok[3]='미나'
print(katok)

# 데이터 삭제 : 사나 삭제 (4등 제거)
katok[4]=None
katok[4]=katok[5]
katok[5]=None
katok[5]=katok[6]
katok[6]=None
del(katok[6]) #빈칸 제거
print(katok)