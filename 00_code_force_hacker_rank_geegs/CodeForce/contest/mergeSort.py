len_list=list(map(int, input().split()))
n=len_list[0]
m = len_list[1]


arr1= list(map(int, input().split()))

arr2 = list(map(int, input().split()))

arr1_pointer=0

arr2_pointer = 0

arr1.append(float('inf'))

arr2.append(float('inf'))

answer = []

for i in range(n+m):
    if arr1[arr1_pointer]<=arr2[arr2_pointer]:
        answer.append(arr1[arr1_pointer])
        arr1_pointer+=1
        
    else:
        answer.append(arr2[arr2_pointer])
        arr2_pointer+=1
        
# while arr1_pointer<n:
#     answer.append(arr1[arr1_pointer])
#     arr1_pointer+=1
# while arr2_pointer<m:
#     answer.append(arr2[arr2_pointer])
#     arr2_pointer+=1
print(* answer)