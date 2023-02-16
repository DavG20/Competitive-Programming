from collections import Counter
def Num_Replacement():
    num_test_case=int(input())

    for _ in range(num_test_case):
        len_test_case=int(input())
        num_input=input().split()
        alpha_input=list(input())
        num_input_count=Counter(num_input)
        alpha_input_count=Counter(alpha_input)
        
        for i in range(len_test_case):
            if alpha_input_count[alpha_input[i]]!=num_input_count[num_input[i]]:
                print("No")
                break
        if i==len_test_case-1:
            print("Yes")
        
        
Num_Replacement()