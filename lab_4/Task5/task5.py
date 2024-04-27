import os

def bfs(vertices, adj_lst, dest):
    visited = [0]*(vertices+1)
    parent_arr = [0]*(vertices+1)
    visited[1] = 1
    parent_arr[1] = -1
    q = []
    q.append(1)
    
    while len(q) != 0:
        node = q[0]
        q.pop(0)        
        for i in adj_lst[node]:
            if visited[i] != 1:
                visited[i] = 1                              #For each visited node, it marks it as visited and updates the parent array
                parent_arr[i] = node                        # with the parent node. This allows us to reconstruct the shortest path later.
                q.append(i)
    
    res = [dest]
    while dest != 1:
        res.append(parent_arr[dest])                        #After the BFS traversal, the function traces back the parent nodes 
        dest = parent_arr[dest]                             #from the destination to the source, building the shortest path in reverse order.
    res.reverse()                                           # that's why we return the res.reverse()
    
    
    return res

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_full_path = os.path.join(script_directory,'input.txt')
    output_full_path = os.path.join(script_directory, 'output.txt')
    
    input_file = open(input_full_path, 'r')
    vertices, edges, dest = [int(value) for value in input_file.readline().split(" ")]
    graph_arr = [ [] for _ in range(vertices+1)]
    
    for _ in range(edges):
      tmp = [int(value) for value in input_file.readline().split(" ")]
      graph_arr[tmp[0]].append(tmp[1])
      graph_arr[tmp[1]].append(tmp[0])
      
    print(dest)  
    shortest_path = bfs(vertices, graph_arr, dest)
    
    output_file = open(output_full_path, 'w')
    output_file.write(f"Time: {len(shortest_path)-1}\nShortest Path: ")
    for elem in shortest_path:
        output_file.write(f"{elem} ")
    output_file.close()

    return 0


if __name__ == "__main__":
    main()
    