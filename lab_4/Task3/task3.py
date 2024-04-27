import os

def dfs_fn(vertices, adj_lst):                # this is a dfs graph traversal using recursion
    visited = [0]*(vertices+1)    
    dfs_arr = []
    node = 1
    
    def dfs(node):
        visited[node] = 1
        dfs_arr.append(node)
        
        for i in adj_lst[node]:
            if(visited[i] != 1):
                dfs(i)
    dfs(node)
    return dfs_arr



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
      graph_arr[tmp[1]].append(tmp[0])
      
    dfs_arr = dfs_fn(vertices, graph_arr)
    
    output_file = open(output_full_path, 'w')
    for elem in dfs_arr:
        output_file.write(f"{elem} ")
    output_file.close()

    return 0


if __name__ == "__main__":
    main()
    