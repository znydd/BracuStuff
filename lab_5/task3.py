def dfs1(node, graph, visited, stk):                    #In Kosaraju's algorithm first I used a depth-first search (DFS) to perform a topological sort 
    visited[node] = 1                                   #of the graph, storing the nodes in a stack in the order of their finishing times.
    for v in graph[node]:                               #then,  performs a DFS on the transpose of the original graph, starting from the nodes in the  
        if visited[v]!= 1:                              #order they were pushed into the stack.
            dfs1(v, graph, visited, stk)                # Each DFS traversal discovers a strongly connected component, which is stored in the scc_lst  
    
    stk.append(node)

def transpose_graph(graph, vertices):
    transposed_graph = [[] for _ in range(vertices+1)]
    for node in range(1, vertices+1):
        for v in graph[node]: 
            transposed_graph[v].append(node)
    return transposed_graph
            

def dfs_scc(node, graph, visited, scc):
    visited[node] = 1
    scc.append(node)
    for v in graph[node]:
        if visited[v]!= 1:
            dfs_scc(v, graph, visited, scc)


def scc(graph, vertices):
    visited = [0]*(vertices+1)
    stk = []
    for i in range(1,vertices+1):
        if visited[i] != 1:
            dfs1(i, graph, visited, stk)
    
    transposed_graph = transpose_graph(graph, vertices)
    
    visited=[0]*(vertices+1)
    scc_lst = []
    
    while stk:
        node=stk.pop()
        if visited[node]!= 1:
            scc = []
            dfs_scc(node, transposed_graph, visited, scc)
            scc_lst.append(scc)
            
    return scc_lst



input_file = open('input3_2.txt', 'r')
output_file = open('output3_2.txt', 'w')
vertices, edges = [int(value) for value in input_file.readline().split(" ")]
adjLst = [[] for _ in range(vertices+1)]
for _ in range(1,edges+1):
    line =[int(value) for value in input_file.readline().split(" ")]
    adjLst[line[0]].append(line[1])    

scc_lst = scc(adjLst, vertices)
scc_lst.sort()
for cc in scc_lst:
    cc.sort()
    for c in cc:
        output_file.write(f"{c} ")
    output_file.write("\n")
output_file.close()
