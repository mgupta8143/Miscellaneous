from collections import deque

class Node:
  def __init__(self, value, neighbors = []):
    self.value = value
    self.neighbors = neighbors
  
  def __repr_(self):
    return "Node(%r)" % self.value

  def connect(self, other):
    self.neighbors.append(other)
    other.neighbors.append(self)
    
def bfs(key, target):
  q = deque([key])
  dic = {key: True}
  while len(q) > 0:
    for n in q[0].neighbors:
      if n == target:
        return True
      if not n in dic:
        q.appendleft(n)
      dic[n] = True
    q.pop()
  return False


n0 = Node(0)
n3 = Node(3)
n4 = Node(4)
n6 = Node(6)
n5 = Node(5)
n7 = Node(7)

n0.connect(n3)
n0.connect(n4)
n6.connect(n3)
n5.connect(n6)

print(bfs(n0,n5))
