#quicksort sorting algorithm

#partition position

def partition(arr,l,h):
    i = ( l - 1 )
    pivot = arr[h]
   
    for j in range( l, h):

        if arr[j] <= pivot:
    
        i = i+1
        arr[i],arr[j] = arr[j],arr[i]
         
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return ( i+1 )
# sort
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        # sort the partitions
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
if __name__ ==
arr = [2,5,3,8,6,5,4,7]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
   print (arr[i],end=" ")