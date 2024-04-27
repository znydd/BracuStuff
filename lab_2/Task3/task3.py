import os


def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_relative_path = "input3.txt"
    output_relative_path = "output3.txt"
    input_full_path = os.path.join(script_directory, input_relative_path)
    output_full_path = os.path.join(script_directory, output_relative_path)

    input_file = open(input_full_path, 'r')
    size = int(input_file.readline())
    arr = []
    for i in range(size):
       arr.append([int(value) for value in input_file.readline().split(" ")])
    
    sorted_list = sorted(arr, key=lambda x: x[1])


    res = [sorted_list[0]]
    finish = sorted_list[0][1]

    for i in range(1,len(arr)):                               # First we have sorted the time range with finishing time 
        if sorted_list[i][0] >= finish:                       # Then we have choosen those pair of time range where the next starting time is equal or greater than
            res.append(sorted_list[i])                        # then previous finishing time 
            finish = sorted_list[i][1]



    output_file = open(output_full_path, 'w')
    output_file.write(f"{len(res)}\n")
    for val in res:
        output_file.write(f"{val[0]}"+" "+f"{val[1]}\n")
    output_file.close()




if __name__ == "__main__":
    main()