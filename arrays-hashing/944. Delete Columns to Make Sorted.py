def minDeletionSize(strs):
    remove_count = 0
    
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if strs[j][i] < strs[j - 1][i]:
                remove_count += 1
                break
    
    return remove_count

print(minDeletionSize(["zyx","wvu","tsr"]))