# deque 자료구조 사용
from collections import deque
print("Input: ",end='')
n,m=map(int,input().split())
# 정답 넣을 리스트 answer
answer=[]

dq=list(range(1,n+1))
dq=deque(dq)

# dq가 빌때 까지 무한반복
while dq:
    for _ in range(m-1):
        # 제일 앞에있는 원소를 pop한 다음
        cur=dq.popleft()
        # 다시 append 그러면 제일 뒤로 간다
        dq.append(cur)
    # m번째가 되면 그 원소를 뺀 다음 리스트에 append
    answer.append(dq.popleft())

answer=', '.join(map(str,answer))

print("result: "+"<"+answer+">")
