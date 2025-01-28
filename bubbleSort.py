def bubble_Sort(arr):
    for i in range(len(arr) -1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr


n=[5,8,6,3,1,5,6,5,6,7]

s=bubble_Sort(n)

print(s)