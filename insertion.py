def insertion_sort(arr):
    
    n = len(arr)
    
    for i in range(1,n):
        key = arr[i]
        j = i-1
        
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j=j-1
        arr[j + 1] = key              
        
myArray = [22,27,16,2,18,6]
insertion_sort(myArray)


print(myArray)

