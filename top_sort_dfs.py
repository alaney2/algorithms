# Top Sort Using DFS
def topological_sort(graph):
  n = len(graph)
  visited = [False] * n
  order = [0] * n
  idx = n - 1

  def dfs(node, visited_nodes):
    visited[node] = True
    for neighbor in graph[node]:
      if visited[neighbor] == False:
        dfs(neighbor, visited_nodes)
    visited_nodes.append(node)
  
  for i in range(n):
    if visited[i] == False:
      visited_nodes = []
      dfs(i, visited_nodes)
      print(visited_nodes)
      for node in visited_nodes:
        order[idx] = node
        idx -= 1
  
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