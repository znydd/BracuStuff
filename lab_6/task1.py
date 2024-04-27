import heapq

def dijkstra(adjList, s):                    #In this problem standard dijkstra shortest path finding algorithm implemented with 
  dist = [float('inf')]*(vertices+1)         #with a priority queue(min heap) to use the smallest distance from source to every node then 
  dist[s] = 0                                #update the distance on dist array, after all element will be finished on the priority queue we
  pq = [(0,s)]                               #will get the shortest path of every node from source node on the dist[i] where i is the target(v) node.

  while len(pq) > 0:
    dis, node= heapq.heappop(pq)

    for v, w in adjList[node]:
      if dis+w < dist[v]:
        dist[v] = dis+w
        heapq.heappush(pq,(dis+w, v))

  dist.pop(0)

  for i in range(len(dist)):
    if dist[i] == float('inf'):
      dist[i] = -1
  return dist



input_file = open("./input1_2.txt", 'r')
vertices, edges = [int(value) for value in input_file.readline().split(" ")]

adjList = [[] for _ in range(vertices+1)]
for _ in range(edges):
  u, v, w = [int(value) for value in input_file.readline().split(" ")]
  adjList[u].append([v,w])
s= int(input_file.readline())
dist = dijkstra(adjList, s)

output_file = open("./output1_2.txt", 'w')

for elem in dist:
  output_file.write(f"{elem} ")
output_file.close()






