# Optimized Bubble sort in Python
def bubbleSort(array):

    # loop through each element of array
    for i in range(len(array)):

        # keep track of swapping
        swapped = False
        print('----------')
        print('i', i)
        print('value', len(array) - i - 1)
        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            print('j', j)

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:

                # swapping elements if elements
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        # no swapping means the array is already sorted
        # so no need for further comparison
        if not swapped:
            break


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
