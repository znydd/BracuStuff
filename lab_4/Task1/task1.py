import os

def adjList(graph_arr, vertices):                         # adjList() creates an adjacency list, which is a dictionary where each key represents a vertex
    res_dict = {}                                   #and the corresponding value is a list of tuples representing the adjacent vertices and their edge weights.
    for i in range(vertices+1):
      res_dict[i] = []

    for j in graph_arr:
      res_dict[j[0]].append((j[1], j[2]))
    
    return res_dict
    

def adjMat(graph_arr, vertices, edges):
  matrix = [[0 for x in range(vertices+1)] for y in range(vertices+1)]  # adjMat() creates an adjacency matrix, where each cell matrix[i][j] represents
                                                                        # the weight of the edge between vertices i and j.
  for i in range(edges):
    matrix[graph_arr[i][0]][graph_arr[i][1]] = graph_arr[i][2]
  return matrix


def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_full_path = os.path.join(script_directory,'input.txt')
    output_full_path1 = os.path.join(script_directory, 'output1.txt')
    output_full_path2 = os.path.join(script_directory, 'output2.txt')
    
    input_file = open(input_full_path, 'r')
    vertices, edges = [int(value) for value in input_file.readline().split(" ")]
    graph_arr = []
    for i in range(edges):
      graph_arr.append([int(value) for value in input_file.readline().split(" ")])
    
    res_mat = adjMat(graph_arr, vertices, edges)
    output_file1 = open(output_full_path1, 'w')
    for i in range(vertices+1):
      for j in range(vertices+1):
        output_file1.write(f"{res_mat[i][j]} ")
      output_file1.write("\n")
    output_file1.close()
    
    
    res_dict = adjList(graph_arr, vertices)
    output_file2 = open(output_full_path2, 'w')
    for k in range(vertices+1):
      if len(res_dict[k]) !=0:
        output_file2.write(f"{k} : {str(res_dict[k]).strip('[]')}\n")
      else:
        output_file2.write(f"{k} : \n")
    output_file2.close()
    
    

    return 0


if __name__ == "__main__":
    main()
    