# 3
# 2 3
# 3 1
# 3 2
# 1 3
# 3 3
# 1 3


# num_test=int(input())

# for i in range(num_test):
#     cut_a=list(map(int,input().split()))
#     cut_b=list(map(int, input().split()))
#     if len(cut_a)<=1:
#         print("No")
#     elif cut_a[0]==cut_b[0] and cut_a[1]+cut_b[1]==cut_a[0]:
#         Print("Yes")
#     elif cut_a[0]==cut_b[1] and cut_a[1]+cut_b[0]==cut_a[0]:
#         print("Yes")
#     elif cut_a[1]==cut_b[0] and cut_a[0]+cut_b[1]==cut_a[1]:
#         print("Yes")
#     elif cut_a[1]==cut_b[1] and cut_a[0]+cut_b[0]==cut_a[1]:
#         print("Yes")
#     else:
#         print("No")'

# num_test=int(input())

# for i in range(num_test):
#     cut_a=list(map(int,input().split()))
#     cut_b=list(map(int, input().split()))
#     if max(cut_a)==max(cut_b) and min(cut_a)+min(cut_b)==max(cut_a):
#         print("Yes")
#     else:
#         print("No")    

# 3
# -1 2 0

len_list=int(input())

num_list=[int(x) for x in input().split()]
print(num_list)

num_list.sort()
print(1,num_list[0])
if num_list[-1]>0:
    print(1,num_list[-1])
    print(len(num_list)-2,*num_list[1:-1])
else:
    print(2,num_list[1],num_list[2])
    print(len(num_list)-3,*num_list[3:])
