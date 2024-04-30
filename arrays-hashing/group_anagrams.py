def sortWord(str):
    return "".join(sorted(str))

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        resultMap = {}
        for str in strs:
            if sortWord(str) not in resultMap:
                resultMap[sortWord(str)] = [str]
            else:
                resultMap[sortWord(str)].append(str)
        
        return list(resultMap.values())
        