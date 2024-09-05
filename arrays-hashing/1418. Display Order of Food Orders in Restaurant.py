def displayTable(orders):
    menu = set()
    tableDict = {}
    tableNum = set()
    
    # create menu list and order per table
    for order in orders:
        menu.add(order[2])
        tableNum.add(int(order[1]))
        
        if int(order[1]) not in tableDict:
            tableDict[int(order[1])] = [order[2]]
        else:
            tableDict[int(order[1])].append(order[2])    
    
    menu = sorted(menu) # sort table
    tableNum = sorted(tableNum) # sort tableNum
    tableDict = dict(sorted(tableDict.items())) # sort table dict
    
    result = [] # list to contains the result
    
    # add first column which contains table and all items of menu
    result.append(["Table"])
    for item in menu:
        result[0].append(item)
    
    for num in tableNum:
        result.append([str(num)])
        
        for item in menu:
            result[len(result) - 1].append(str(tableDict[num].count(item)))
    
    return result
        

orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
print(displayTable(orders))