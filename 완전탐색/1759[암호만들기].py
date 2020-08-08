def check(combStr):
    vowel = 0
    consonant = 0
 
    for char in combStr:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1
        else:
            consonant += 1
 
    if consonant >= 2 and vowel >= 1:
        return True
    else:
        return False
 
 
def solution(L, inputList, combStr, index):
 
    if len(combStr) is L:
        if check(combStr) is True:
            print(''.join(combStr))
        return;
 
    if index >= len(inputList): 
        return;
 
    solution(L, inputList, combStr+list(inputList[index]), index + 1)
    solution(L, inputList, combStr, index + 1)
 
 
answer = 0
L, C = map(int, input().split())
inputList = list(map(str, input().split()))
inputList.sort()
 
combStr = []
index = 0

print(inputList)
solution(L, inputList, combStr, index)





https://covenant.tistory.com/124




from itertools import combinations
L, C = map(int, input().split())
a = sorted(input().split())
for s in combinations(a, L):
    passwd = ""
    vowel, consonant = 0, 0
    for i in range(len(s)):
        if s[i] in "aeiou":
            vowel += 1
        else:
            consonant += 1
        passwd += s[i]
        if vowel >= 1 and consonant >= 2:
            print(passwd)


 https://rebas.kr/688 

 

                   









items = [1,2,3,4,5]
print(list(permutations(items,2)))
output-> [(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), 
                (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)]

순서를 고려 -> AB와 BA를 서로 다른 것으로 여긴다 
AB, AC, AD
BA, BC, BD
CA, CB, CD
DA, DB, DC

print(list(combinations(items,2)))
output -> [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]


순서를 고려하지 않는다. -> AB, BA는 다른 것
AB, AC, AD
    BC, BD
        CD





