class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            temp = s
            s = t
            t = temp

        hashTable = {}
        for char in s:
            if char in hashTable:
                hashTable[char] += 1
            else:
                hashTable[char] = 1
        
        for char in t:
            if char not in hashTable:
                return False
            else:
                if hashTable[char] == 0:
                    return False
                hashTable[char] -= 1

        return True
        

        