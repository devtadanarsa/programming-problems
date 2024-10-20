def numberOfEmployeesWhoMetTarget(hours, target):
    return len([x for x in hours if x >= target])

