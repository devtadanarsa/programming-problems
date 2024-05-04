class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}
        for idx, num in enumerate(numbers):
            hashTable[num] = idx
            
        for idx, num in enumerate(numbers):
            temp = target - num
            if temp in hashTable:
                return [idx + 1, hashTable[temp] + 1]
        
        return [-1, 0]