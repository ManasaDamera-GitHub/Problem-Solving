def power_of_n(val,power):
    res=0
    res=res+val+val
    if power==0:
        return 1
    else:
        for i in range(power-2):
            res=res+res
    return res

print(power_of_n(2,5))