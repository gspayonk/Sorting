# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        for j in range(cur_index, len(arr)):
            if arr[j]< arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    counter = 0
    for i in range(1, len(arr)):
        for j in range(1, len(arr) - counter):
            if arr[j] < arr[j - 1]:
                pos1 = arr[j - 1]
                pos2 = arr[j]
                arr[j - 1] = pos2
                arr[j] = pos1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum = -1 ):
    if len(arr) == 0: return arr
    min_value = max_value = arr[0]

    #find min and max variables
    for v in range(len(arr)):
        if arr[v] < 0: return 'Error'
        elif arr[v] < min_value: min_value = arr[v]
        elif arr[v] > max_value: max_value = arr[v]
    
    #create empty list of n size
    count_arr = [0] * (max_value - min_value + 1)

    #do the counting
    for n in range(len(arr)):
        count_arr[arr[n] - min_value] += 1

    #sort array
    arr = []
    for i in range(len(count_arr)):
        for n in range(count_arr[i]):
            arr.append(i + min_value)

    return arr