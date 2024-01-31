import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

case = list(map(int,input().split()))

max_value = 0
stack = [[case[0], case[0]]]

for i in range(1, N):
    temp = 0
    while stack and case[i] < stack[-1][0]:
        temp += stack[-1][1]
        max_value = max(max_value, stack[-1][0] * temp)
        stack.pop()
    temp += case[i]
    stack.append([case[i], temp])
        
temp = 0
while stack:
    temp += stack[-1][1]
    max_value = max(max_value, stack[-1][0] * temp)
    stack.pop()

print(max_value)
