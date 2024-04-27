import os


def merge(a, b, c):
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
        
    for x in b:
        c = max(a[-1] + x**2, c)                # Here to find max A[i] + A[j]^2 we need to use the max of a which is a[-1] as sortred, also b[-1] for b[j] but the element in b can be  
                                                # negative and negative value can be in front if there is positive value in b. So, we need to check all the value of b then take the max one
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1

    return [arr,c]


def maxValMergeSort(arr):
    if len(arr) <= 1:
        return [arr,float("-inf")]
    else:
        mid = len(arr)//2;
        a1 = maxValMergeSort(arr[:mid])
        a2 = maxValMergeSort(arr[mid:])
        return merge(a1[0], a2[0], max(a1[1],a2[1])) # only taking the max sum 



def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_full_path = os.path.join(script_directory, "input.txt")
    output_full_path = os.path.join(script_directory, "output.txt")

    input_file = open(input_full_path, 'r')
    size = int(input_file.readline())
    arr = [int(value) for value in input_file.readline().split(" ")]


    res_count = maxValMergeSort(arr)

    output_file = open(output_full_path, 'w')
    output_file.write(f"{res_count[1]}")
    output_file.close()
    return 0


if __name__ == "__main__":
    main()