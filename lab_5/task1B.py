def kahnTopoSort(adjLst, vertices):  # Here kahns algorithm were used for topological sort using BFS where used the concept of ingegree also check DAG
    
    #Indegree
    indegree = [0]*(vertices+1)
    for i in adjLst:
        for j in i:
            indegree[j]+=1

    #BFS
    q = []
    res = []
    for i in range(1,vertices+1):
        if indegree[i] == 0:
            q.append(i)

    while len(q) != 0:
        node = q[0]
        q.pop(0)
        res.append(node)

        for j in adjLst[node]:
            indegree[j]-=1
            if indegree[j] == 0:
                q.append(j)                             
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

input_file = open('input1b_3.txt', 'r')
output_file = open('output1b_3.txt', 'w')
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