import sys
input = sys.stdin.readline

N = int(input())
height = [int(input()) for _ in range(N)]

stack = []      # (키, cnt)로 append
ans = 0

for h in height:

  # 스택 끝 값보다 키 크면 pop
  while stack and stack[-1][0] < h:
    ans += stack.pop()[1]

  # 스택이 비어있으면 해당 키 append하고 continue
  if not stack:
    stack.append((h, 1))
    continue

  # 스택 끝 값의 키와 같을 때
  if stack[-1][0] == h:
    cnt = stack.pop()[1]
    ans += cnt

    if stack: 
        ans += 1
    stack.append((h, cnt+1))

  # 스택 끝 값의 키보다 작을 때
  else:
    stack.append((h, 1))
    ans += 1

# 결과값 출력
print(ans)