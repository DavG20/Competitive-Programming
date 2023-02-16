
def countingValleys(setps,path):
    vallyValue=0
    mount_value=0
    count_Vally=[]
    count=0
    SeaLevel=0
    for step in path:
        count_Vally.append(SeaLevel)
        if step=="D":
            vallyValue-=1
            SeaLevel=mount_value+vallyValue
            
        elif step=="U":
            mount_value+=1
            SeaLevel=mount_value+vallyValue
    count_Vally.append(SeaLevel)
    for i in range(len(count_Vally)-1):
        if count_Vally[i]==0 and count_Vally[i+1]<0:
            count+=1

    return count_Vally, count

    
            
        