import os


def partition(arr, low, high):
    pivot = arr[high]
   
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1



def quickSort(arr, low, high):                              # Normal quici sort where we assuming the pivot as the right most value
    if low < high:
        pivot_index = partition(arr, low, high)
       
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)

    return arr




def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_full_path = os.path.join(script_directory, "input.txt")
    output_full_path = os.path.join(script_directory, "output.txt")

    input_file = open(input_full_path, 'r')
    size = int(input_file.readline())
    arr = [int(value) for value in input_file.readline().split(" ")]


    res_count = quickSort(arr, 0, size-1)

    output_file = open(output_full_path, 'w')
    for elem in res_count:
        output_file.write(f"{elem} ")
    output_file.close()

    return 0


if __name__ == "__main__":
    main()