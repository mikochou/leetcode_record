#建一个num以及后一位比它大的字典
def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        for i,num1 in enumerate(nums2):
            for num2 in nums2[i+1:]:
                if num1<num2:
                    d[num1] = num2
                    break
        return [d.get(num1,-1) for num1 in nums1]