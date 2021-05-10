N =6
inp=[["A", "B"],["A", "C"],["A", "D"],["B", "E"], ["D", "E"],["F", "H"],["F", "G"],["I", "J"]]
e =["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K" ]
mg ={}
for i in e:
  mg[i]=[]
for u, v in inp:
  mg[u].append(v)
  mg[v].append(u)
  
print(mg)

 
def dfs(node, g, visited):
  visited.add(node)
  s = 0
  for child in g[node]:
    if child not in visited:
      s=s+dfs(child,g, visited)
  return s+1
  
visited = set()
a =[]
for i in e:
  if i not in visited:
    t = dfs(i, mg,visited)
    a.append(t)
print(a)