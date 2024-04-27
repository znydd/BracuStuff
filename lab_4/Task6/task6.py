import os



def floodFill(row, col, rows, cols, trsr_map):
    if row < 0 or row >= rows or col < 0 or col >= cols or trsr_map[row][col] == '#':       #The floodFill function takes the current 
        return 0                                                                       # position (row, col) and checks if it's a valid position
    cnt = 0                                                                            #on the map and if the cell is unexplored (not '#').
    if trsr_map[row][col] == 'D':
        cnt+=1
                                                                                #If the current cell contains a diamond ('D'), it increments a counter (cnt)
    trsr_map[row][col] = '#'                                                    #It marks the current cell as visited ('#') and recursively calls floodFill 
                                                                                #on all valid adjacent cells (up, down, left, right).
    cnt += floodFill(row+1, col, rows, cols, trsr_map)
    cnt += floodFill(row-1, col, rows, cols, trsr_map)
    cnt += floodFill(row, col+1, rows, cols, trsr_map)
    cnt += floodFill(row, col-1, rows, cols, trsr_map)
                                                                                #The recursion continues until all connected cells containing diamonds are explored
    return cnt                                                                  # then the final count is returned.



def dimondCollector(trsr_map, rows, cols):
    dimondMax = 0
    for row in range(rows):
        for col in range(cols):
            if trsr_map[row][col] == ".":
                dimond = floodFill(row, col, rows, cols, trsr_map)     # Here we iterate every possible ways of finding dimond and take the max one
                dimondMax = max(dimond, dimondMax)
    
    return dimondMax




def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_full_path = os.path.join(script_directory,'input.txt')
    output_full_path = os.path.join(script_directory, 'output.txt')
    
    input_file = open(input_full_path, 'r')
    rows, cols = [int(value) for value in input_file.readline().split(" ")]
    trsr_map = []
    for _ in range(rows):
        trsr_map.append([value  for value in input_file.readline().strip("\n")])
  
    res = dimondCollector(trsr_map, rows, cols)
    print(res)
    
    return 0


if __name__ == "__main__":
    main()
    