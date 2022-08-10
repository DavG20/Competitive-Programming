class Solution(object):
    def nextGreaterElement(self,nums1,nums2):
        output=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    print(nums1[i], j)
                    k=j+1
                    if j<(len(nums2)-1):
                        store=0
                        while k<(len(nums2)):
                            print(nums2[k],"num k")
                            if nums1[i]<nums2[k]:
                                print(nums1[i],"nums i")
                                store=(nums2[k])
                                k=len(nums2)
                            elif nums1[i]>nums2[k]:
                                k+=1
                                print("ss",k)
                                if (k==len(nums2)):
                                    store=-1
                            else:
                                store=-1
                        output.append(store)
                    else:
                        output.append(-1)
        return(output)
                
c=Solution()
c.nextGreaterElement([4,1,2], [1,3,4,2,6])
