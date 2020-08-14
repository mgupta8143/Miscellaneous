from collections import deque

class Node:
  def __init__(self, value, neighbors = []):
    self.value = value
    self.neighbors = neighbors

  def __repr(self):
    return "Node(%r)" % self.value
  
  def connect(self, other):
    self.neighbors.append(other)
    other.neighbors.append(self)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.connect(n2)

def bfs(key, target):
  q = deque([key])
  dic = {key: True}
  while len(q) > 0:
    for n in q[0].neighbors:
      if n == target:
        return True
      if not n in dic:
        q.append(n)
        dic[n] = True
    q.popleft()
  return False

print(bfs(n1, n2))
