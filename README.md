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

```

### [상미](<./오아시스 재결합/상미.py>)

```py

```

### [병국](<./오아시스 재결합/병국.py>)

```py

```

### [성구](<./오아시스 재결합/성구.py>)

```py

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
