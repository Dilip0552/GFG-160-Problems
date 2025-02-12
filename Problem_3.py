arr=[2,5,7,23,8,9,1]
n=len(arr)
temp_arr=[]
for i in range(n-1,-1,-1):
    temp_arr.append(arr[i])
for i in range(n):
    arr[i]=temp_arr[i]
print(arr)