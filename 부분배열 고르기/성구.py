# 2104 부분배열 고르기 - 힌트봄
import sys
input = sys.stdin.readline


def solution():
    # 누적합 알고리즘 + stack + 최대최장수열
    # 누적합 알고리즘
    #   임의의 수 i, j에 대해 둘을 인덱스로 갖는 리스트에서
    #   i까지의 누적합 - j 까지의 누적합 = j~i 사이의 누적합

    # 구현
    # 1. 누적합리스트와 원본 리스트
    # 2. 반복문을 통해 돌면서 stack에 최솟값을 저장
    # 3. 이번에 넣을 수가 이전 수보다 작으면 최솟값 비교 -> 최솟값이 같으면 무조건 증가(요소 범위: 0 이상)
    # 4. 최솟값을 비교하며, 이전 최댓값부터 현재 값까지의 누적합에 현재 넣을 수보다 큰 애들을 곱해 을 통해 최댓값 비교
    N = int(input())
    arr = list(map(int, input().split()))
    # default setting
    # 누적합 리스트(prefix) 와 본리스트 (arr)
    arr.append(0)
    prefix = [0] * (N+1)
    prefix[1] = arr[0]
    for i in range(1, N):
        prefix[i+1] = arr[i] + prefix[i]
    
    # 비교 리스트 stack
    stack = []
    # 최댓값 비교 대상
    maxv = arr[0] ** 2
    for i in range(N+1):
        tmp = arr[i]
        last_max_idx = i
        # 만약 최솟값 후보가 들어오면(이전 값보다 작으면)
        while stack and stack[-1][0] > tmp:
            # 이전 최솟값 후보들과 비교하면서 거기까지 최솟값 * 누적합
            minv, last_max_idx = stack.pop()
            # 최댓값 비교
            maxv = max(maxv, minv *(prefix[i]-prefix[last_max_idx]))
        # 현재 값: 최솟값 후보
        # stack에 넣을 값: 최솟값 후보, 최장수열의 최댓값
        stack.append((tmp, last_max_idx))
    
    print(maxv)

if __name__ == "__main__":
    solution()  
