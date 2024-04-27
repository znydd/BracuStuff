import heapq

def dijkstra(adjList, s):
  dist = [float('inf')]*(vertices+1)
  dist[s] = 0
  pq = [(0,s)]

  while len(pq) > 0:
    dis, node= heapq.heappop(pq)

    for v, w in adjList[node]:        #Here insted of putting distance on the dist array we put the min value from max of other path from
        mx = max(dist[node], w)       #source to that index node and at the end index we get the min value from all max of every path from souce to end 
        if mx < dist[v]:
            dist[v] = mx
            heapq.heappush(pq,(dist[v], v))

  dist.pop(0)

  for i in range(len(dist)):
    if dist[i] == float('inf'):
      dist[i] = -1
  
  return dist[-1]



input_file = open("./input3_2.txt", 'r')
vertices, edges = [int(value) for value in input_file.readline().split(" ")]

adjList = [[] for _ in range(vertices+1)]
for _ in range(edges):
  u, v, w = [int(value) for value in input_file.readline().split(" ")]
  adjList[u].append([v,w])

path = dijkstra(adjList, 1)

output_file = open("./output3_2.txt", 'w')
if path == -1:
    output_file.write("Impossible")
else:
    output_file.write(f"{path}")
    
output_file.close()






