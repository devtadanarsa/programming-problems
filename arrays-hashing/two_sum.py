class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numCount = {}
        numIdx = {}

        for index, num in enumerate(nums):
            if num not in numIdx:
                # numCount[num] = 1
                numIdx[num] = [index]
            else:
                # numCount[num] += 1
                numIdx[num].append(index)

        for num in nums:
            remainder = target - num
            if remainder not in numIdx:
                continue
            else:
                if len(numIdx[num]) >= 2:
                    return [numIdx[num][0], numIdx[num][1]]
                else:
                    if num != remainder :
                        return [numIdx[num][0], numIdx[remainder][0]]
                    continue
        
        return 0