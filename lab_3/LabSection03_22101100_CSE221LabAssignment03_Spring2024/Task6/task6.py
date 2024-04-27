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


def quickSort(arr, low, high, q):
    if low <= high:
        pivot_index = partition(arr, low, high)                     # According to query we are only finding the correct position for the those queries so we are only 
                                                                    # doing recursion on that part where our query lies, not doing recursion where our query isnt in range. For 1-based index we used q-1
        if pivot_index == q - 1:
            return arr[pivot_index]
        elif pivot_index > q - 1:
            return quickSort(arr, low, pivot_index - 1, q)
        else:
            return quickSort(arr, pivot_index + 1, high, q)
   


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_full_path = os.path.join(script_dir, 'input.txt')
    output_full_path = os.path.join(script_dir, 'output.txt')

    input_file = open(input_full_path, 'r')
    arr_size = int(input_file.readline())
    arr = [int(value) for value in input_file.readline().split(" ")]
    query_size = int(input_file.readline())
    queries = [int(value) for value in input_file.read().split("\n")]

    output_file = open(output_full_path, 'w')
    for query in queries:
        res = quickSort(arr, 0, arr_size-1, query)
        output_file.write(f"{res}\n")
    output_file.close()


    return 0

if __name__ == "__main__":
    main()