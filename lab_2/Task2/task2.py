import os


def sol_nlogn(arr1, size1, arr2, size2):
    arr = arr1 + arr2   
    arr.sort() #Python .sort() which time complexity is nlogn
    return arr
    

def sol_n(left_half, size1, right_half, size2):   # Here I have used the the part of merge sort which merge two sorted array and it is O(n)
    left_half = [1, 3, 5, 7]
    right_half = [2, 2, 4, 8]
    arr = [0]*size1+size2
    i = j = k = 0
    while i < size1 and j < size2:
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < size1:
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < size2:
        arr[k] = right_half[j]
        j += 1
        k += 1
    return arr





def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_relative_path = "input2.txt"
    output1_nlogn_rel_path = "output2_nlogn.txt"
    output1_On_rel_path = "output2_On.txt"
    input_full_path = os.path.join(script_directory, input_relative_path)
    output1_nlogn_full_path = os.path.join(script_directory, output1_nlogn_rel_path)    
    output1_On_full_path = os.path.join(script_directory, output1_On_rel_path)    

    input_file = open(input_full_path, 'r')
    size1 = int(input_file.readline())
    arr1 = [int(value) for value in input_file.readline().split(" ")]
    size2 = int(input_file.readline())
    arr2 = [int(value) for value in input_file.readline().split(" ")]

    res_nlogn = sol_nlogn(arr1, arr2)
    output_file1 = open(output1_nlogn_full_path, 'w')
    for value in res_nlogn:
        output_file1.write(f"{value} ")
    output_file1.close()

    res_n = sol_n(arr1,size1, arr2, size2)
    output_file2 = open(output1_On_full_path, 'w')
    for value in res_n:
        output_file2.write(f"{value} ")
    output_file2.close()





if __name__ == "__main__":
    main()