import sys

input = sys.stdin.readline

E,S,M = map(int,input().split())

earth, sun, moon, result = 1,1,1,1




while True:
    if earth == E and sun == S and moon == M:
       break
  
    earth+=1
    sun+=1
    moon+=1
    result+=1

    if earth>=16:
        earth-=15
    if sun>=29:
        sun-=28
    if moon>=20:
        moon-=19

    
print(result)