def topologicalSort(adjLst, vertices):      #Here DFS were used for topological sort where the dfs went to the full depth of the graph then 
    visited = [0]*(vertices+1)              #during back tracking it stored the vertices value on a stack. So, it stored where dfs visited and finished
    stack = []                              #then if we pop from the top of the stack we will get the topological sort 
    def dfs(node):
        visited[node] = 1
        for i in adjLst[node]:
            if visited[i] != 1:
                dfs(i)
        stack.append(node)


    for i in range(1,len(adjLst)):
        if visited[i] != 1:
            dfs(i)
    stack.reverse()
    return stack       


def isCyclic(adjLst, vertices):   # Here we checked is there any cycle in the graph because topological sort only works on DAG or directed acyclic graph
    visited = [0]*(vertices+1)    # if there is cycle then there will be no topological sort
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

input_file = open('input1a_3.txt', 'r')
output_file = open('output1a_3.txt', 'w')
vertices, edges = [int(value) for value in input_file.readline().split(" ")]
adjLst = [[] for _ in range(vertices+1)]
for _ in range(1,edges+1):
    line =[int(value) for value in input_file.readline().split(" ")]
    adjLst[line[0]].append(line[1])


if isCyclic(adjLst, vertices):
    output_file.write("IMPOSSIBLE")
else:    
    res = topologicalSort(adjLst, vertices)
    for val in res:
        output_file.write(f"{val} ")
    
output_file.close()