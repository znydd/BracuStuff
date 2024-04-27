import os


def sol_n2(arr, size, target):
    for i in range(size):
        for j in range(size):
            if arr[i]+arr[j] == target: # Trivial O(n^2) solution
                return f"{i+1} {j+1}"
    return -1



def sol_n(arr, size, target):
    low = 0
    high = size - 1
    while low <= high:
        if arr[low]+arr[high] == target:     # Here we used 2 pointer method where the pointers were moved based on the summation of their index value
            return f"{low+1} {high+1}"       # so we can reach to target value
        elif arr[low]+arr[high] > target:
            high-=1
        else:
            low+=1
    return -1




def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_full_path = os.path.join(script_directory, "input1.txt")
    output1_On2_full_path = os.path.join(script_directory, "output1_On2.txt")    
    output1_On_full_path = os.path.join(script_directory, "output1_On.txt")    


    input_file = open(input_full_path, 'r')
    size, target =[int(value) for value in input_file.readline().split(" ")]
    arr = [int(value) for value in input_file.readline().split(" ")]
    
    res_n2 = sol_n2(arr, size, target)
    output_file1 = open(output1_On2_full_path, 'w')
    output_file1.write(res_n2)
    output_file1.close()


    res_n = sol_n(arr, size, target)
    output_file2 = open(output1_On_full_path, 'w')
    output_file2.write(res_n)
    output_file2.close()


if __name__ == "__main__":
    main()