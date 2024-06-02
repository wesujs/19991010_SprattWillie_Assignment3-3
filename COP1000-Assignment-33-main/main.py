# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

year = None
month = None
day = None



def isValidDate(year, month, day):
    validDate = True
    MIN_YEAR = 0
    MIN_MONTH = 1
    MAX_MONTH = 12
    MIN_DAY = 1
    MAX_DAY = 31
    
    # Get the year, then the month, then the day
    # housekeeping()

    # Check to be sure date is valid

    if int(year) <= MIN_YEAR: # invalid year
        validDate = False
    elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
        validDate = False
    elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
        validDate = False
    elif int(month) == 11 and int(day) > 30:
            validDate = False
    # Test to see if date is valid and output date and whether it is valid or not

    # endOfJob()
    if validDate == True:
        # Output statement
        return f'{month}/{day}/{year} is a valid date'
    else:
        # Output statement
        return f'{month}/{day}/{year} is an invalid date'
    

month = input("Enter in a month: ")
day = input("Enter in a day: ")
year = input("Enter in a year: ")


print(isValidDate(year, month, day))