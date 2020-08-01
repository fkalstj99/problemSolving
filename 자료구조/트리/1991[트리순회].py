import sys

sys.setrecursionlimit(10**6)





def preorder(node):

    if node== '.':
      return
    print(node, end="")

    preorder(tree[node][0])
    preorder(tree[node][1])

#10 6 3 8 15 20



def inorder(node):
    if node== '.':
      return
    inorder(tree[node][0])
    print(node, end="")
    inorder(tree[node][1])

def postorder(node):
    if node== '.':
      return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end="")
  





tree = {}
n = int(input())
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')



#DFS -> Depth First search
#preorder -> root left child right child
#Inorder -> left child root right child
#postOrder -> left child right child  root
#        10
#    6       15
#3     8           20