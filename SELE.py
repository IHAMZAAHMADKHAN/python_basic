def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
             min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]    

    return arr 


n=[3,5,9,74,3,5,4,6]

p=selection_sort(n)
print(p)