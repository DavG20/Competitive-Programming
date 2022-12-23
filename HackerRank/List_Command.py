if __name__ == '__main__':
    N = int(input())
    ans_list=[]
    
    for i in range(N):
        curr_command=input().split(" ")
        if curr_command[0]=="append":
            ans_list.append(int(curr_command[1]))
        if curr_command[0]=="insert":
            ans_list.insert(int(curr_command[1]),int(curr_command[2]))
        if curr_command[0]=="pop":
            ans_list.pop()
        if curr_command[0]=="remove":
            ans_list.remove(int(curr_command[1]))
        if curr_command[0]=="reverse":
            ans_list.reverse()
        if curr_command[0]=="print":
            print(ans_list)
        if curr_command[0]=="sort":
            ans_list.sort()
