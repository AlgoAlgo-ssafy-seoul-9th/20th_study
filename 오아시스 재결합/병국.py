from collections import deque

n = int(input())

arr = deque()

for _ in range(n):
    person = int(input())
    arr.append(person)

cnt = 0
tmp_arr = []

for person in arr:

    # 대기열에 있고, 마지막애보다 지금들어올 애가 크면
    # 4 - 1 있는데 2 들어오면 1 빼고 cnt += 1
    # 4 남았으니까 cnt += 1
    # 4 - 2 - 2 있는데 5 들어오면 2, 2, 4 빼고 cnt += 3
    # 남은거 없으니까 cnt += 0

    while tmp_arr and tmp_arr[-1] < person:
        # print(tmp_arr,'빼기전',person)
        tmp_arr.pop()
        # print(tmp_arr,'빼고난후')
        cnt += 1
    # 있으면 다 추가해주기
    cnt += len(tmp_arr)
    # print(tmp_arr,'남은거 뭔지')
    tmp_arr.append(person)
    # print(tmp_arr,cnt)


print(cnt)
