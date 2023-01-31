# def Organize():
#     num_test=int(input())
#     for _ in range(num_test):
#         words=input()
        
#         word_list=words.split()
#         ans=["" for _ in range(len(word_list))]
#         for i in range(len(word_list)):
#             new_word=""
#             num=0
#             for char in word_list[i]:
#                 if char.isnumeric():
#                     num=int(char)
#                 else:
#                     new_word+=char
#             ans[num-1]=new_word
#         print("".join(ans))
            
                    
                    
                    
# Organize()
# 10
# 4664 6496 5814 7010 5762 5736 6944 4850 3698 7242



# def Organize():
#     num_test=int(input())
#     for _ in range(num_test):
#         words=input()
        
#         word_list=words.split()
#         ans=["" for _ in range(len(word_list))]
#         for i in range(len(word_list)):
#             new_word=""
#             num=0
#             for char in word_list[i]:
#                 if char.isnumeric():
#                     num=int(char)
#                 else:
#                     new_word+=char
#             ans[num-1]=new_word
#         print("".join(ans))
# Organize()




# def Contest():
#     num_contest=int(input())
#     contest_list=input().split()
#     count=0
#     for i in range(len(contest_list)-1):
#         if contest_list[0]<contest_list[1]:
#             if contest_list[i]<contest_list[i+1]:
#                 count+=1
#             else:
#                 for j in range(i+1,len(contest_list)):
#                     if contest_list[i]<contest_list[j]:
#                         count+=1
#                         break
#         else:
#             if contest_list[i]>contest_list[i+1]:
#                 count+=1
#             else:
#                 for j in range(i+1,len(contest_list)):
#                     if contest_list[i]>contest_list[j]:
#                         count+=1
#                         break
#     print(count)
# Contest()
            
                



                # 10
# 4664 6496 5814 7010 5762 5736 6944 4850 3698 7242

def Contest():
    num_test=int(input())
    num_list=input().split()
    if len(num_list)<=1:
        print(0)
        return
        

    ans=[num_list[0]]
    if num_list[0]<num_list[1]:
        for i in range(1,len(num_list)):
            if num_list[i]>ans[-1]:
                ans.append(num_list[i])
        print(len(ans))
    elif num_list[0]>num_list[1]:
        for i in range(1,len(num_list)):
            if num_list[i]>ans[-1]:
                ans.append(num_list[i])
        print(len(ans))
    
        
Contest() 
            
            
            
            
        
        