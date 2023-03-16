
# Do not change any of the code below

def days_in_month(year, month):
    pass


#This is a line of code changed
def is_leapYear(year):
    for i in range(len(year)):
        print(year[i])
        if (year[i] % 4 == 0 and year[i] % 100 != 0) or (
                year[i] % 4 == 0 and year[i] % 100 == 0 and year[i] % 400 == 0):

            return True
        else:
            return False



year = int(input("Enter a year:"))
month = int(input("Enter a month"))



days = days_in_month(year,month)
print(days)





        
