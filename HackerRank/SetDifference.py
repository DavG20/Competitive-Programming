num_stud_english=int(input())
English_sec=input().split()
num_stud_french=int(input())
French_sec=input().split()
count=0
for student in English_sec:
    if student not in French_sec:
        count+=1
        
print(count)