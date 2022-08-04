

class Solutions(object):
    def AddTwoNumbers(self,l1,l2):
        reminder=0
        store=[]
        data=[len(l1),len(l2)]
        for i in range(max(data)-min(data)):
            if(len(l1)==max(data)):
                l2+=[0]
            elif (len(l2)==max(data)):
                l1+=[0]
            else:
                break
        for i in range(max(data)):
            if((((l1[i]+l2[i])%10 )+reminder)!=10):
                store +=[((l1[i]+l2[i])%10 )+reminder]
                reminder=(l1[i]+l2[i])//10
                print(reminder,"inside the =10")
            elif ((((l1[i]+l2[i])%10 )+reminder)==10):
               store+= [(((l1[i]+l2[i])%10 )+reminder)%10]
               reminder =(((l1[i]+l2[i])%10 )+reminder)//10
               print(reminder,'inside the >10')
            
                
        store+=[reminder]
          
            
        
        

            

c=Solutions()
c.AddTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])