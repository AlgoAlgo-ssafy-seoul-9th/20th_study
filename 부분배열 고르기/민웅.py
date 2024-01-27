# 2104_부분배열고르기_Select a partial sequence
import sys
input = sys.stdin.readline

N = int(input())

seq = list(map(int, input().split()))
# 4
# 1 1 1 9
# 가장 끝 원소도 계산해야함.
seq.append(0)

ans = seq[0]*seq[0]
partial_sum = [seq[0]]
for i in range(1, N):
    temp = partial_sum[-1] + seq[i]
    partial_sum.append(temp)
# 첫 부분까지 다 누적합인경우를 위해 끝에 0 추가
partial_sum.append(0)
stack = []

for i in range(N+1):
    num = seq[i]
    idx = i
    while stack and stack[-1][0] > num:
        tmp_num, idx = stack.pop()
        ans = max(ans, tmp_num*(partial_sum[i-1]-partial_sum[idx-1]))

    stack.append((seq[i], idx))

print(ans)









