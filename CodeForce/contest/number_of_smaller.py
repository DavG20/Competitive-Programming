len_list=list(map(int, input().split()))
len_arr1=len_list[0]
len_arr2=len_list[1]

arr1=list(map(int, input().split()))

arr2=list(map(int, input().split()))

arr1_pointer=0
arr2_pointer=0

answer=[]

while arr1_pointer < len(arr1) and arr2_pointer < len(arr2):
    if arr1[arr1_pointer]<arr2[arr2_pointer]:
        arr1_pointer+=1
    else:
        arr2_pointer+=1
        answer.append(arr1_pointer)
while arr2_pointer<len(arr2):
    answer.append(arr1_pointer)
    arr2_pointer+=1
print(*answer)
        
        
    