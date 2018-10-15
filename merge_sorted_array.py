class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        p1 = m
        p2 = n
        for i in range(m + n - len(nums1)):
            nums1[i + m + n] = 0
        while p1 > 0 or p2 > 0:
            if p1 == 0: 
                nums1[p2+p1-1] = nums2[p2-1]
                p2 -= 1
            elif p2 == 0:
                nums1[p2+p1-1] = nums1[p1-1]
                p1 -= 1
            elif nums1[p1-1] > nums2[p2-1]:
                nums1[p2+p1-1] = nums1[p1-1]
                p1 -= 1
            elif nums1[p1-1] <= nums2[p2-1]:
                nums1[p2+p1-1] = nums2[p2-1]
                p2 -= 1

        return nums1
print Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print Solution().merge([2,0], 1, [1], 1)
