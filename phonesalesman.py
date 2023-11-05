############## Problem  2 #################### 
#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.

monthlySalesList = [5,23,21,14,23,12,4,12,22,22,34,12]  # Sample number of phones sold in each month in a year
#FillinMissingCode - initialise all the variables needed
base_monthly_salary=10000     
bonus_for_5phone_sold=5000
bonus_after_first_5phone_sold=1100
for month, phoneCount in enumerate(monthlySalesList):
    #calculate the Salary using If stmts
    #FillinMissingCode
    if phoneCount>=5:
       currentMonthSalary = base_monthly_salary+bonus_for_5phone_sold+(phoneCount-5)*bonus_after_first_5phone_sold#FillinMissingCode
       print (f"This month's salary before additional bonus {currentMonthSalary}") 

    #check for condition #If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
    # this month also, then he gets additional Rs5000.
    if (phoneCount>=20) and (base_monthly_salary>=20000):
        currentMonthSalary+=5000
    if(phoneCount < 20):
        previousMonthSalary = currentMonthSalary #we set this so that, we can use this info in the next iteration
        continue #no need to calculate anything because <20 phones sold
    
#calculate the new salary
currentMonthSalary = previousMonthSalary  #FillinMissingCode
print(f"This month's salary after additional bonus {currentMonthSalary}")
previousMonthSalary = currentMonthSalary #Why are we doing this?

'''
OUTPUT:

This month's salary before additional bonus 15000
This month's salary before additional bonus 34800
This month's salary before additional bonus 32600
This month's salary before additional bonus 24900
This month's salary before additional bonus 34800
This month's salary before additional bonus 22700
This month's salary before additional bonus 22700
This month's salary before additional bonus 33700
This month's salary before additional bonus 33700
This month's salary before additional bonus 46900
This month's salary before additional bonus 22700
This month's salary after additional bonus 22700
'''