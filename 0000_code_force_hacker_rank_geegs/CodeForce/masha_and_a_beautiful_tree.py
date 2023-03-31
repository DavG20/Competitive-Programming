
def mergeSort(nums , count ):

    if len(nums) == 1:
        return nums
    
    else:

        left = 0

        right = len(nums) - 1

        mid = left + (right - left)//2

        num_l = nums[:mid + 1]

        num_r = nums[mid + 1:]

        

        l , r  , k = 0 ,0 ,0
        
        print(num_l , num_r, )
        if num_l[0] <= num_r[0] and num_l[-1] <= num_r[0]:
            count += 1
            print(nums,num_l , num_r)
            print(num_l+num_r)
            
            return num_l+num_r
        elif num_r[0] < num_l[0] and num_r[-1] < num_l[0]:
            print("in here" , num_l , num_r)
            count += 1
            print(nums,num_r, num_l)
            print(num_r+num_l)
            return num_r + num_l  
        elif num_l[0] <= num_r[0] and num_l[-1] > num_r[0] or num_r[0] < num_l[0] and num_r[-1] > num_l[0]:
            return -1

        else:
            # return num_r + num_l
            print("in here")
            return

        
            



t = int(input())


for _ in range(t):

    m = int(input())

    nums = list(map(int , input().split()))

    if nums == sorted(nums):
        print(0)
        break
    else:
        mergeSort(nums  ,0)

    


