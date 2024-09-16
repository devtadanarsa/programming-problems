def countSeniors(details):
    count = 0
    for detail in details:
        if int(detail[11]) > 6:
            count += 1
            continue
        elif int(detail[11]) == 6:
            if int(detail[12]) > 0:
                count += 1
            
    return count

print(countSeniors(["2941701174O9078"]))
print(int("2941701174O9078"[11]))