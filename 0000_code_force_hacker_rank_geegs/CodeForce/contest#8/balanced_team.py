def sol():
    n = int(input())
    
    students = list(map(int, input().split()))
    
    students.sort()
    
    left = 0
    
    right = 0
    
    max_ = 0
    
    while left  < n: 
        
        while right < n and students[right]- students[left] <= 5:
            right += 1
        max_ = max(max_ , right - left)
        
        left += 1
        right += 1
    print(max_)
sol()
    
    
# n = int(input())

# num1 = list(map(int, input().split()))

# num2 = list(map(int, input().split()))

# count = 0
# i = 0
# while  i < (n):
#     j = i +  1
#     while j < n:
#         if num1[i] + num1[j] > num2[i] + num2[j]:
#             count += 1
# print(count)

