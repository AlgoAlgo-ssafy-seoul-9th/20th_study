# 20th_study

### 20주차 알고리즘스터디

# 이번주 문제

<details open>
<summary>접기/펼치기</summary>
<div markdown="1">

## [부분배열 고르기](https://www.acmicpc.net/problem/2104)

### [민웅](<./부분배열 고르기/민웅.py>)

```py
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

```

### [상미](<./부분배열 고르기/상미.py>)

```py

```

### [병국](<./부분배열 고르기/병국.py>)

```py

```

### [성구](<./부분배열 고르기/성구.py>)

```py

```

### [승우](<./부분배열 고르기/승우.py>)

```py

```

## [오아시스 재결합](https://www.acmicpc.net/problem/3015)

### [민웅](<./오아시스 재결합/민웅.py>)

```py
# 3015_오아시스재결합_Oasis-reunion
import sys
input = sys.stdin.readline

N = int(input())

fans = []
idx = 0
ans = 0
max_h = 0
while True:
    if idx == N:
        break

    h = int(int(input()))
    if not fans:
        # 스택 비었으면 추가
        # max_h 갱신
        fans.append([h, 1])
        max_h = h
    else:
        # 새로 들어온 사람 키가 더 크면
        if h > fans[-1][0]:
            # 스택이 남아있고, 앞사람키가 더 작으면 정답쌍(해당키 사람 수만큼) 늘려주고 pop
            while fans and fans[-1][0] < h:
                tmp = fans[-1][1]
                ans += tmp
                fans.pop()
            # pop 하다가 아직 fans 남았는데, 키가 같은사람이면 그 사람들까지 정답쌍 추가하고 해당 요소에 인원추가
            if fans and fans[-1][0] == h:
                tmp = fans[-1][1]
                ans += tmp
                fans[-1][1] += 1
            else:
                fans.append([h, 1])
            # 만약 지금 들어온사람이 지금까지 최고키가 아니면 추가로 한쌍추가(제일 큰애가 얘 볼수있음)
            if h < max_h:
                ans += 1

        elif h == fans[-1][0]:
            tmp = fans[-1][1]
            ans += tmp
            fans[-1][1] += 1
            if h < max_h:
                ans += 1
        else:
            if fans:
                ans += 1
            fans.append([h, 1])
        if h > max_h:
            max_h = h

    idx += 1


print(ans)

```

### [상미](<./오아시스 재결합/상미.py>)

```py

```

### [병국](<./오아시스 재결합/병국.py>)

```py

```

### [성구](<./오아시스 재결합/성구.py>)

```py
# 3015 오아시스 재결합 - 힌트 보고함
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
```

### [승우](<./오아시스 재결합/승우.py>)

```py

```

</div>
</details>
<br><br>

# 알고리즘 설명

<details>
<summary>접기/펼치기</summary>

</details>
