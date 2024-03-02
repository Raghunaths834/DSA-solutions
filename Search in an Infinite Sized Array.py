def binary_search(arr,key,l,r):
    if l<= r:
        mid = (l+(r-l)) // 2 
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            return binary_search(arr,key,mid+1,r)
        return binary_search(arr,key,l,mid-1)
    return -1
        
    
def findPos(arr,k):
    if arr[0] == k:
        return 0 
    i = 1 
    while arr[i] < k:
        i *=2 
    if arr[i] == k:
        return i 
    return binary_search(arr,key,i//2 + 1,i-1)
    
    
arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
ans = findPos(arr,10)
if ans == -1:
	print ("Element not found")
else:
	print("Element found at index",ans)
