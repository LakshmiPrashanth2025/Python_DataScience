import numpy as np

arr = np.array([1,2,3,4])
print(arr)


a  = np.array([1,2,3,4,5])
b = np.array([10,20,30,40,50,60])

print(a[0])
print(b[3])
print(a[1:5])

total = sum(a)     # Returns 30
maximum = max(a)   # Returns 10
minimum = min(a)   # Returns 2

print(f"Sum: {total}, Max: {maximum}, Min: {minimum}")



b_reshaped= b.reshape(3,2)
print("Reshaped array b", b_reshaped)

# 2d array
user_arr = np.array([[1,2],[3,4]] )
print('user array', user_arr)
print('user array shape ', user_arr.shape)
print('user array datatype ', user_arr.dtype)
print('user array dimension ', user_arr.ndim)
print('user array size ', user_arr.size)

filtered_b = b[b> 30]
print("Filtered Array" , filtered_b)



array_unsorted=np.array([50,40,100,20,10,20,30])
print("Sorted Array" , np.sort(array_unsorted))

print("Unique Elements Array" , np.unique(array_unsorted))

x = np.array([50,40,100,20,10,20,30])
y = np.array([150,140,200,120,110,120,130])
result = np.concatenate((x,y))
print("Concatenated Array" , result)




