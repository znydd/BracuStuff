import heapq

def dijkstra(adjList, s):
  dist = [float('inf')]*(vertices+1)
  dist[s] = 0
  pq = [(0,s)]

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



input_file = open("./input2_3.txt", 'r')
vertices, edges = [int(value) for value in input_file.readline().split(" ")]

adjList = [[] for _ in range(vertices+1)]
for _ in range(edges):
  u, v, w = [int(value) for value in input_file.readline().split(" ")]
  adjList[u].append([v,w])
alice, bob = [int(value) for value in input_file.readline().split(" ")]

aliceDist = dijkstra(adjList, alice)        #Here for Alice and Bob dijkstra was used to find the shortest path of all nodes from     
bobDist = dijkstra(adjList, bob)            #their location and also detected those nodes where they can't reach. 
time = float("inf")                          
node = 0                                   #After on this loop below I have taken the perfect place for meet by iterating over all the 
                                          # node's shortest path then selected that node where the max time between Alice and Bob is the  
for i in range(len(aliceDist)):           #shortes also skipped where -1 or unreachable
    if aliceDist[i] == -1 or bobDist[i] == -1:
        continue
    if max(aliceDist[i], bobDist[i]) < time:
        time = max(aliceDist[i], bobDist[i])
        node = i+1
        
    
output_file = open("./output2_3.txt", 'w')
if time == float("inf"):
    output_file.write("Impossible")
else:
    output_file.write(f"Time {time}\nNode {node}")

output_file.close()






