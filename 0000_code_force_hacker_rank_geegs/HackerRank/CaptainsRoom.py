from collections import Counter
num_group=int(input())
room_li=input()
room_li=room_li.split(" ")
count=Counter(room_li)
val=count.most_common()
print(val[-1][0])