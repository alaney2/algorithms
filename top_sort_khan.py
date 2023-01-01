from collections import deque

# Top Sort Using Khan's Algorithm
def topological_sort(graph):
  n = len(graph)
  degrees = [0] * n
  print(n, degrees)
  for i in range(n):
    for neighbor in graph[i]:
      degrees[neighbor] += 1
  
  queue = deque()
  for i, degree in enumerate(degrees):
    if degree == 0:
      queue.append(i)
  print(degrees)
  idx = 0
  order = [0] * n
  while (queue):
    node = queue.popleft()
    order[idx] = node
    idx += 1
    for neighbor in graph[node]:
      degrees[neighbor] -= 1
      if degrees[neighbor] == 0:
        queue.append(neighbor)

  if idx != n:
    return None # graph contains cycle  

  return order

graph = { 
  0: [1,3], 
  1: [], 
  2: [0, 4], 
  3: [1], 
  4: [3, 5], 
  5: [1] 
}
print(topological_sort(graph))