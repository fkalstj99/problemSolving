#트리의 지름 구하는 공식 
#1. 임의의 하나의 노드 A에서 가장 거리먼 노드 B를 구하고
#2. B에서 가장 거리가 먼 노드 C를 구했을때
#3. B와 C사이의 거리가 트리의 지름이다.
import sys

input = sys.stdin.readline

V = int(input())
#트리 정점의 개수 

matrix = [[] or _ in range(V+1)]

