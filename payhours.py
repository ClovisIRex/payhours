import datetime,colorama
now = datetime.datetime.now()
today = now.today().day

holidays = [] #[datetime.date(2013, 8, 14)] -add holidays here
restDays = [4,5]
businessdays = 0
REQUIRED_WORKING_HOURS_EACH_DAY = 9
lastday = 0
for i in range(1, 32):
    try:
        thisdate = datetime.date(now.year, now.month, i)
        lastday = i
    except(ValueError):
        break
    if thisdate.weekday() not in restDays and thisdate not in holidays:
        businessdays += 1
total = businessdays * REQUIRED_WORKING_HOURS_EACH_DAY

alreadyDone = 126.35 # Change this every day
dayleft = lastday - today
print "---------------------------"
print colorama.Fore.YELLOW + "Total number of hours to work this month: {}".format(total)
print colorama.Fore.GREEN + "Total number of hours already done this month: {}".format(alreadyDone)
print colorama.Fore.RED + "Number of hours left to work this month: {}".format(total-alreadyDone)
print colorama.Fore.LIGHTRED_EX + "Number of days left to work this month: {}".format(dayleft)
print colorama.Fore.MAGENTA + "Average of hours left to work each day this month: {}".format((total-alreadyDone)/float(dayleft))
print colorama.Fore.RESET + "---------------------------"
