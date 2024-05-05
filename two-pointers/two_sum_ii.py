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

    def twoSumTwoPointer(numbers, target):
        ptrOne, ptrTwo = 0, len(numbers) - 1
        
        while ptrOne < ptrTwo:
            if numbers[ptrOne] + numbers[ptrTwo] == target:
                return [ptrOne + 1, ptrTwo + 1]
            elif numbers[ptrOne] + numbers[ptrTwo] < target:
                ptrOne += 1
            elif numbers[ptrOne] + numbers[ptrTwo] > target:
                ptrTwo -= 1
        
        return [ptrOne, ptrTwo]
        