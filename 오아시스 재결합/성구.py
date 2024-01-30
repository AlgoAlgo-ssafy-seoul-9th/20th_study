# 3015 오아시스 재결합
import sys
input = sys.stdin.readline


def solution():
    stack = []
    cnt = 0
    for _ in range(int(input())):
        fan = int(input())
        # 만약 나보다 작은 수가 stack에 들어있으면 pop
        # cnt += 갯수만큼
        while stack and fan > stack[-1][0]:
            cnt += stack.pop()[1]
        # 스택에 요소가 남아있으면, 나보다 큰 사람이 있으면
        if stack:
            # 키 비교
            if fan == stack[-1][0]:
                # 나와 같은 키가 있을 때
                # 그 수만큼을 더함(이 사람들은 나와 보이는 사람들)
                cnt += stack[-1][1]
                # 만약 그 뒤에 다른 사람이 있다면 그사람도 추가
                if len(stack) > 1:
                    cnt += 1
                # 키가 같은 사람 수 ++
                stack[-1][1] += 1
            else:
                # 작은 경우는 없고 큰 경우만 있으며,
                # 큰 경우 이 사람과 나는 무조건 보이기에 +1
                stack.append([fan, 1])
                cnt += 1
        else:
            # 스택이 비어있으면 추가
            stack.append([fan, 1])

    print(cnt)

if __name__ == "__main__":
    solution()