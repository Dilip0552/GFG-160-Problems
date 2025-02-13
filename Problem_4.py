                # This Approach takes more time 
# arr=[1,2,3,4,5,6,7]
# d=4
# for i in range(d):
#     first=arr[0]
#     for j in range(len(arr)-1):
#         arr[j]=arr[j+1]
#     arr[len(arr)-1]=first

# print(arr)
                # Takes less time (more efficient code)
arr=[1,2,3,4,5,6,7]
d=2
d=d%len(arr)
temp_arr=[0]*len(arr)
temp_arr[:len(arr)-d+1]=arr[d:]
temp_arr[len(arr)-d:]=arr[:d]
print(temp_arr)