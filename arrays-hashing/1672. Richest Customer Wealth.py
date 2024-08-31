def maximumWealth(accounts):
    wealthiest = 0
    
    for account in accounts:
        wealthiest = max(wealthiest, sum(account))
        
    return wealthiest
