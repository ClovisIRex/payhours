import datetime,colorama

REQUIRED_WORKING_HOURS_EACH_DAY = 9

now = datetime.datetime.now()
today = now.today().day
holidays = []
restDays = [4,5]
businessdays = 0
lastday = 0

while True:      
    try:
        alreadyDone = float(raw_input("Enter number of hours already done: \n"))
    except Exception:
        print "Invalid number!"
        continue
    break

isVacations = str(raw_input("Did you take day-offs? (enter y for yes, anything else for no): \n"))

if isVacations is "y":
    while True:
        try:
            vacation = int(raw_input("Enter day-off/holidays/vacations this month in day's number(e.g 11 for 11th of this month): \n"))
        except Exception:
            print "Invalid number!"
            continue
        holidays.append(datetime.date(now.year,now.month,vacation))
        isMore = str(raw_input("More days?(enter y for yes, anything else for no): \n"))
        if isMore is not "y":
            break

for i in range(1, 32):
    try:
        thisdate = datetime.date(now.year, now.month, i)
        lastday = i
    except(ValueError):
        break
    if thisdate.weekday() not in restDays and thisdate not in holidays:
        businessdays += 1
total = businessdays * REQUIRED_WORKING_HOURS_EACH_DAY

dayleft = lastday - today + 1


print "---------------------------"
print "Total number of hours to work this month: {}".format(total)
print "Total number of hours already done this month: {}".format(alreadyDone)
print "Number of hours left to work this month: {}".format(total-alreadyDone)
print "Number of days left to work this month: {}".format(dayleft)
print "Average of hours left to work each day this month: {}".format((total-alreadyDone)/float(dayleft))
print "---------------------------"
raw_input("Press any key to exit...")