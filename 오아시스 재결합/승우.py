import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

stack = []
count = 0
for i in range(1, N+1):
    cur_input = int(input())
    while stack:
        if stack[-1][0] < cur_input:
            count += 1
            count += stack[-1][2]
            stack.pop()
            continue
        elif stack[-1][0] == cur_input:
            count += 1
            count += stack[-1][2]
            stack[-1][2] += 1
            if len(stack) != 1:
                count += 1
                break
            else:
                break
        else:
            count += 1
            stack.append([cur_input, i, 0])
            break

    if len(stack) == 0:
        # 겹쳤을 경우 세번째 변수에 1씩 추가
        stack.append([cur_input, i, 0])

print(count)
