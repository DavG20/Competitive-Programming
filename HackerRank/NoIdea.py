from collections import Counter
happiness=0
m_n=input()
n_num=input()
mn_list=m_n.split(" ")
m=int(mn_list[1])
n=int(mn_list[0])
array=n_num.split(" ")
A=input().split(" ")
B=input().split(" ")
countA=Counter(A)
countB=Counter(B)
for num in array:
    happiness+=countA[num]
    happiness-=countB[num]
print(happiness)