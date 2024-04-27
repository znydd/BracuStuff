import os

def bfs(vertices, adj_lst):                   # This is a bfs graph traversal using queue
    visited = [0]*(vertices+1)
    visited[1] = 1
    q = []
    q.append(1)
    bfs_arr = []
    
    while len(q) != 0:
        node = q[0]
        q.pop(0)
        bfs_arr.append(node)
        
        for i in adj_lst[node]:
            if visited[i] != 1:
                visited[i] = 1
                q.append(i)
    return bfs_arr

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
      
        
    bfs_arr = bfs(vertices, graph_arr)
    
    
    output_file = open(output_full_path, 'w')
    for elem in bfs_arr:
        output_file.write(f"{elem} ")
    output_file.close()

    return 0


if __name__ == "__main__":
    main()
    