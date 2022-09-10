def merge_sort(inp_arr):
    size = len(inp_arr)
    if size > 1:
        middle = size // 2
        left_arr = inp_arr[:middle]
        right_arr = inp_arr[middle:]
        print(inp_arr)
        merge_sort(left_arr)
        merge_sort(right_arr)

 


# Driver Code
if __name__ == '__main__':
    arr = [8, 3, 6, 1, 9, 7, 2, 5]
    merge_sort(arr)
    print(arr)



