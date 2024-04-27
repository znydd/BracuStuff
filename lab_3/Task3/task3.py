import os


def merge(a, b, c):
    i = j = k = 0
    arr = [0]*(len(a)+len(b))
    while len(a) > i and len(b) > j:
        if a[i] < b[j]:
            arr[k] = a[i]
            i+=1
        else:                                       # Here we i < j is already maintained as we are comparing a[i] as left array and b[j] as right array 
            arr[k] = b[j]                           # in case of H[i] > H[j] we are adding the count only when a[i] > a[j] which is all the element after a[i]
            c+=len(a)-i
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

    return [arr,c]


def pairsMergeSort(arr):
    if len(arr) <= 1:
        return [arr,0]
    else:
        mid = len(arr)//2;
        a1 = pairsMergeSort(arr[:mid])
        a2 = pairsMergeSort(arr[mid:])
        return merge(a1[0], a2[0], a1[1]+a2[1])



def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_full_path = os.path.join(script_directory, "input.txt")
    output_full_path = os.path.join(script_directory, "output.txt")

    input_file = open(input_full_path, 'r')
    size = int(input_file.readline())
    arr = [int(value) for value in input_file.readline().split(" ")]


    res_count = pairsMergeSort(arr)

    output_file = open(output_full_path, 'w')
    output_file.write(f"{res_count[1]}")
    output_file.close()

    return 0


if __name__ == "__main__":
    main()