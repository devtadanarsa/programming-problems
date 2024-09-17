def twoEditWords(queries, dictionary):
    res = []
    
    for query in queries:
        for word in dictionary:
            diff = 0
            for i in range(len(query)):
                if query[i] != word[i]:
                    diff += 1
                    if diff > 2:
                        break
                
            if diff <= 2:
                res.append(query)
                break
    
    return res

queries = ["word","note","ants","wood"]
dictionary = ["wood","joke","moat"]
print(twoEditWords(queries, dictionary))
            