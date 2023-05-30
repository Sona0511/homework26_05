# A year is a leap year if it is divisible by 4,except that years divisble by 100are not leap years 
#unless they are also divisible by 400. Ask the user to enter a year and using the // operator, 
#determine how many leap years there have been between 1600 and that year. 

#4+400-100
def count_div4 (start,end,divisor):
    divisor=4
    count = 0
    for num in range(start,end+1):
        if num %divisor ==0:
            count+=1
    return count