def sort(arr):
    n=len(arr)
    for i in range (n):
        for j in range(i+1,n):
         if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
            
    return arr  


n=[2,6,3,2,1]

result= sort(n)

print(result)