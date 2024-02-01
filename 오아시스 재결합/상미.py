## 백준_ 3015_ 오아시스 재결합

import sys
input = sys.stdin.readline

num_ppl = int(input()) # 사람의 수

stack = [] # [(높이, 개수)]
answer = 0

# 계속 감소하는 수열 만들기

for _ in range(num_ppl):

    person = int(input())    

    if not stack or person < stack[-1][0]: # 스택이 비어 있거나, 더 작은 경우
        stack.append([person, 1])

    elif person == stack[-1][0] : # 같을 경우

        # 같은 높이와의 매칭
        answer += stack[-1][1]
        stack[-1][1] += 1

    else: # 더 클 경우

        # 왼쪽으로 가면서 작은 애들과의 연결고리 만들기
        while stack and person > stack[-1][0]: # 높이가 같아질 때까지 계속 반복
            answer += stack.pop()[-1]
        
            # 작은 친구들 다 뺐을 때, 같은 애들이 있다면 묶기
        if stack and person == stack[-1][0]:
            answer += stack[-1][1]
            stack[-1][1] += 1

        else:
            stack.append([person, 1])

    if len(stack) > 1:
        answer += 1

print(answer)