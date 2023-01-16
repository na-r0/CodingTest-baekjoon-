# 문제
# 조기 졸업을 꿈꾸는 종욱이는 요즘 핫한 딥러닝을 공부하던 중,
# 이미지 처리에 흔히 쓰이는 합성곱 신경망(Convolutional Neural Network, CNN)의 풀링 연산에 영감을 받아 자신만의 풀링을 만들고 이를 222-풀링이라 부르기로 했다.
# 종욱이는 N×N 행렬에 222-풀링을 반복해서 적용하여 크기를 1×1로 만들었을 때 어떤 값이 남아있을지 궁금해한다.

# 입력
# 첫째 줄에 N(2 ≤ N ≤ 1024)이 주어진다. N은 항상 2의 거듭제곱 꼴이다. (N=2K, 1 ≤ K ≤ 10)
# 다음 N개의 줄마다 각 행의 원소 N개가 차례대로 주어진다. 행렬의 모든 성분은 -10,000 이상 10,000 이하의 정수이다.

# 출력
# 마지막에 남은 수를 출력한다.

# 4
# -6 -8 7 -4
# -5 -5 14 11
# 11 11 -1 -1
# 4 9 -2 -4

import sys

data = []
N = int(sys.stdin.readline())
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))

def solution(data, num):
    if num==1: return data[0][0]
    re = [[] for _ in range(num//2)]
    for i in range(0,num,2):
        for j in range(0,num,2):
            re[i//2].append(sorted([data[i][j], data[i+1][j], data[i][j+1], data[i+1][j+1]])[2])
    return solution(re, num//2)

print(solution(data, N)) # 답: 11