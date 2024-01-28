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
