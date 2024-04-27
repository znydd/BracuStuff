import os


def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_full_path = os.path.join(script_directory, "input4.txt")
    output_full_path = os.path.join(script_directory, "output4.txt")

    input_file = open(input_full_path, 'r')
    size , friend = [int(value) for value in input_file.readline().split(" ")]

    arr = []
    for i in range(size):
        tmp = []
        for value in input_file.readline().split(" "):
            tmp.append(int(value))
        arr.append(tmp)
    
    sorted_list = sorted(arr, key=lambda x: x[1])
    res = 0
    for _ in range(friend): 
        track = [0]
        res+=1
        finish = sorted_list[0][1]
        for i in range(1,len(sorted_list)):
            if sorted_list[i][0] >= finish:     
                res+=1
                track.append(i)
                finish = sorted_list[i][1]
        for j in reversed(track):                          #WE poped those pair which is already some person used for classes then did the most class fucntion again with 
            sorted_list.pop(j)                              # Reversed(track) for popping the bigger index first so no left sift can effect   
        track = []



    output_file = open(output_full_path, 'w')
    output_file.write(f"{res}")
    output_file.close()



if __name__ == "__main__":
    main()