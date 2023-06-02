# A year is a leap year if it is divisible by 4,except that years divisble by 100are not leap years 
#unless they are also divisible by 400. Ask the user to enter a year and using the // operator, 
#determine how many leap years there have been between 1600 and that year. 
def count_4div(start,end): 
    count =0
    for num in range (start,end+1):
        if num % 4==0 and (num% 100!=0 or num%400==0):
            count+=1
    return count
start=1600
end=input("enter the year")
end=int(end)
result =count_4div(start,end)
print (result)
