def subdomainVisits(cpdomains):
    dict = {}
    
    for cp in cpdomains:
        temp = cp.split(" ")
        count = int(temp[0])
        domain = temp[1].split(".")
        
        if len(domain) == 2:
            names = [domain[0] + "." + domain[1], domain[1]]
            for name in names:
                if name not in dict:
                    dict[name] = 0
                
                dict[name] += count
        else:
            names = [domain[0] + "." + domain[1] + "." + domain[2], domain[1] + "." + domain[2], domain[2]]
            for name in names:
                if name not in dict:
                    dict[name] = 0
                
                dict[name] += count
        
    res = []
    for key in dict:
        res.append(str(dict[key]) + " " + key)
    
    return res

print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))