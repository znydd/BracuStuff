import os

def merge(a, b):
    i = j = k = 0
    arr = [0]*(len(a)+len(b))
    while len(a) > i and len(b) > j:
        if a[i] < b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1

    return arr


def mergeSort(arr):          # Normal merge sort where the merge fucntion take 2 sorted fucntion then add them into one sorted fucntio
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2;
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)
    

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_full_path = os.path.join(script_directory, "input.txt")
    output_full_path = os.path.join(script_directory, "output.txt")

    input_file = open(input_full_path, 'r')
    size = int(input_file.readline())
    arr = [int(value) for value in input_file.readline().split(" ")]
   
    sorted_arr = mergeSort(arr)

    output_file = open(output_full_path, "w")
    for elem in sorted_arr:
        output_file.write(f"{elem} ")
    output_file.close()
    return 0


if __name__ == "__main__":
    main()