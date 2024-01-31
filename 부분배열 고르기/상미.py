# 백준_ 2104_ 부분배열 고르기

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
s = 0
stack = []

for i in range(N):
    width = 0
    # 새로 들어오는 수가 stack의 마지막 수보다 작으면 비교 들어감
    while stack and nums[i] < stack[-1][0]:
        width += stack[-1][1]
        s = max(s, width * stack[-1][0])
        stack.pop()

    width += nums[i]
    stack.append((nums[i], width))

width = 0
while stack:
    width += stack[-1][1]
    s = max(s, width * stack[-1][0])
    stack.pop()

print(s)
