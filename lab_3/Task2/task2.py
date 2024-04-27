import os


def findMax(arr):         # Here the findMax fucntion use diveide and conquer method and divide the array into 1 length array and from there it just return the greater value
                         # which at the end return the max value of the array  
    if len(arr) <= 1:
        return arr[0]
    else:
        mid = len(arr)//2

        max_left = findMax(arr[:mid]) 
        max_right = findMax(arr[mid:])

        return max(max_left, max_right)



def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_full_path = os.path.join(script_directory, "input.txt")
    output_full_path = os.path.join(script_directory, "output.txt")

    input_file = open(input_full_path, 'r')
    size = int(input_file.readline())
    arr = [int(value) for value in input_file.readline().split(" ")]
    max_res = findMax(arr)
    
    output_file = open(output_full_path, 'w')
    output_file.write(f"{max_res}")
    output_file.close()



    return 0

if __name__ == "__main__":
    main()