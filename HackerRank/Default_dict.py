from collections import defaultdict
len_input=input().split()
len_groupA,len_groupB=int(len_input[0]),int(len_input[1])
groupA_dict=defaultdict(list)
for i in range(len_groupA):
    input_chr=input()
    groupA_dict[input_chr].append(i+1)
for i in range(len_groupB):
    input_b=input()
    output=groupA_dict[input_b]
    print(*output) if output else print(-1)