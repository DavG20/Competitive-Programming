# num_student=int(input())
# for _ in range(num_student):
#     student_info=input().split("#")
#     readable_info=" ".join(student_info)
#     print(readable_info)

# 4
# Nazrawi Haile Brok Fitsum
# Haile Fitsum

num_student=int(input())
student_list=input().split(" ")
flaged_member=input().split(" ")
count=0
for good_student in student_list:
    if good_student not in flaged_member and len(good_student)==len(set(good_student)):
        count+=1
print(count)