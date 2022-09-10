def merge_sort(inp_arr):
    size = len(inp_arr)
    if size > 1:
        middle = size // 2
        left_arr = inp_arr[:middle]
        right_arr = inp_arr[middle:]
 
        merge_sort(left_arr)
        merge_sort(right_arr)
 
        p = 0
        q = 0
        r = 0
 
        left_size = len(left_arr)
        right_size = len(right_arr)
        while p < left_size and q < right_size:
            if left_arr[p] < right_arr[q]:
                inp_arr[r] = left_arr[p]
                p += 1
            else:
                inp_arr[r] = right_arr[q]
                q += 1
            print("-->", inp_arr)
            r += 1
 
        
        while p < left_size:
            inp_arr[r] = left_arr[p]
            p += 1
            r += 1
 
        while q < right_size:
            inp_arr[r]=right_arr[q]
            q += 1
            r += 1

        print("---->", inp_arr)


# Driver Code
if __name__ == '__main__':
    arr = [8, 3, 6, 1, 9, 7, 2, 5]
    merge_sort(arr)
    print(arr)



