class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1,n2=len(nums1),len(nums2)
        i=0
        j=0

        prev=0
        cur=0
        for _ in range(((n1+n2)//2)+1):
            prev=cur
            if i<n1 and j<n2:
                if nums1[i]<=nums2[j]:
                    cur=nums1[i]
                    i+=1
                else:
                    cur=nums2[j]
                    j+=1
            elif i<n1:
                cur=nums1[i]
                i+=1
            else:
                cur=nums2[j]
                j+=1
            print(prev,cur)

        if (n1+n2)%2==1: 
            return cur
        print(prev,cur)
        return (prev+cur)/2