def router__house(distance):
    router = 1
    cur_house = house[0]

    for i in range(1, N):
      if cur_house + distance <= house[i]:
        cur_house = house[i]
        router+=1

    return router 


N, C = map(int,input().split())
house = [int(input()) for _ in range(N)]

house.sort()

start, end = house[0], house[-1] - house[0]
# 최소거리 , 최대거리 


while start <= end:
  mid = (start+end)//2

  if router__house(mid) >= C:
    answer = mid
    start = mid + 1
  else:
    end = mid - 1

print(answer)



파라메트릭 서치 (Parametric Search)

가능한 해의 최솟값, 최댓값을 구하라는 문제에서 사용됨



이진탐색 -> 주어진 일련의 값들에서 구함

파라메트릭 서치  -> 주어진 범위 내 원하는 값 , 원하는 조건에서 가장 일치하는 값을

ex)

이진탐색 -> 정렬된 값 중 middle이 내가 찾는 값인지가 중요

파라메트릭 서치 -> 내가 "설정"한 조건에 맞는 값을 찾는 것이다. 
               -> 결국 내가 조건을 "설정"해야한다.
               -> 최적화문제 = 이진탐색 + 결정문제(Yes or No) 쪼갬 



기본 뼈대 

1. 이진 탐색 이용 -> 임의의 값 계산 (보통 mid값)

2. 이 값은 문제 조건을 만족하나 안하나? 

3. 문제 조건 만족할시 -> 저장해두고 , 범위를 좁혀가면서 최적화된 해에 도달 


전제 조건 

1. 해의 구간이 연속적이어야함

2. mid가 문제 조건 만족하면 -> [start, mid] or [mid, end] 범위 해는 

모두 문제 조건을 만족할만한 '가능성'이 있어야함

5가 mid값이라면 start ~ mid < 5 and mid ~ end > 5