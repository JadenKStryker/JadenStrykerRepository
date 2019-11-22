#sum() will add up all the numbers in the list based on variable b and its
#cycling through the list and meeting coditions.
#range() will tell sum to iterate 1000 times.
#because no initial start value is given sum() will begin at 0

a = sum(b for b in range(1000) if b % 3 == 0 or b % 5 == 0)
print (f"the sum of all numbers under 1000 which are divisble by 3 or 5 is {a}")
    
