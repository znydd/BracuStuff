import os

def cycle_check(vertices, adj_lst):                 #cycle_check() uses a nested function ckDfs to perform the DFS traversal
    visited = [0]*(vertices+1)                      #keeping track of visited nodes and nodes in the current recursion path.
    same_path = [0]*(vertices+1)                    #During the DFS traversal, if a node is encountered that has already been visited 
                                                    #and is present in the current recursion path, it means a cycle has been detected.
    
    def ckDfs(node):
        visited[node] = 1
        same_path[node] = 1
                
        for i in adj_lst[node]:
            if(visited[i] != 1):
                if ckDfs(i) == True:
                    return True
            elif same_path[i] == 1:
                return True
                
        same_path[node] = 0
        return False
    
    for i in range(1,vertices+1):                   
        if visited[i] != 1:
            if ckDfs(i) == True:
                return True
        
    return False
            



def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_full_path = os.path.join(script_directory,'input.txt')
    output_full_path = os.path.join(script_directory, 'output.txt')
    
    input_file = open(input_full_path, 'r')
    vertices, edges = [int(value) for value in input_file.readline().split(" ")]
    graph_arr = [ [] for _ in range(vertices+1)]
    
    for _ in range(edges):
      tmp = [int(value) for value in input_file.readline().split(" ")]
      graph_arr[tmp[0]].append(tmp[1])
    #   graph_arr[tmp[1]].append(tmp[0])
    print(graph_arr)
    isCycle = cycle_check(vertices, graph_arr)
    print(isCycle)
    output_file = open(output_full_path, 'w')
    if isCycle:
        output_file.write("YES")
    else:
        output_file.write("NO")
        
    output_file.close()

    return 0


if __name__ == "__main__":
    main()
    