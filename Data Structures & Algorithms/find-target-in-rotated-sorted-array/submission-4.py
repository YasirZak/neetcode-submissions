class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n==1: return 0 if nums[0]==target else -1
        s=0
        e=n-1
        while True:
            mid = math.floor((s+e)/2)
            if (mid==0 and nums[0]<nums[1]) or \
            (mid==n-1 and nums[-1]<nums[-2]) or \
            (nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]):
                s = mid
                break
            if nums[mid]>nums[e]:
                if s==mid:
                    s=e
                    break
                s = mid
            else:
                e = mid

        print(f"Start found: {s}")
        gap = n
        while True:
            gapMid = math.ceil(gap/2)
            i = (s+gapMid)%n
            if gapMid==1:
                if nums[s]==target:
                    return s
                if nums[i]==target:
                    return i
                break
            if nums[i]==target:
                return i
            if nums[i]<target:
                s = i
            gap = gapMid

        return -1

