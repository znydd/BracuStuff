from queue import PriorityQueue


def kahnTopoSort(adjLst, vertices):   #This the same as Kahn's topological sort with BFS but here insted of queue I used priority queue or min heap so it picks the
    indegree = [0]*(vertices+1)       # smallest value and keep the sort lexicographically smaller than other variations of topo sort

    for i in adjLst:
        for j in i:
            indegree[j]+=1

    pq = PriorityQueue()
    res = []
    for i in range(1,vertices+1):
        if indegree[i] == 0:
            pq.put(i)

    while not pq.empty():
        node = pq.get()
        res.append(node)

        for j in adjLst[node]:
            indegree[j]-=1
            if indegree[j] == 0:
                pq.put(j)                             
    return res


def isCyclic(adjLst, vertices):
    visited = [0]*(vertices+1)
    path = [0]*(vertices+1)    
    
    def dfs(node):
        visited[node] = 1
        path[node] = 1
        for i in adjLst[node]:
            if visited[i] != 1:
                if dfs(i) == True:
                    return True
            elif path[i] == 1:
                return True
        path[node] = 0
        return False
    
    for i in range(1,len(adjLst)):
        if visited[i] != 1:
            if dfs(i) == True: return True
    return False

input_file = open('input2_3.txt', 'r')
output_file = open('output2_3.txt', 'w')
vertices, edges = [int(value) for value in input_file.readline().split(" ")]
adjLst = [[] for _ in range(vertices+1)]
for _ in range(1,edges+1):
    line =[int(value) for value in input_file.readline().split(" ")]
    adjLst[line[0]].append(line[1])        
        
if isCyclic(adjLst, vertices):
    output_file.write("IMPOSSIBLE")
else:    
    res = kahnTopoSort(adjLst, vertices)
    for val in res:
        output_file.write(f"{val} ")
    
output_file.close()