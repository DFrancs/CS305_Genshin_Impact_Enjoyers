import time
import sys

#dishes = mon, wed, fri
#floors, bathrooms, surfaces = 2nd(at most 14th)/4th(at most 28th) wed
#trash, recycling = wed, sun
#refrigerator = 3rd fri

#currentTime = time.asctime()

#daymonthdate = list(currentTime.split(" "))

def calBuild(day, date):

	daymonthdate = [day,"Dec",date]

	daystilwed = 0

	if daymonthdate[0] != "Wed":
		if daymonthdate[0] == "Mon":
			daystilwed = 2
		elif daymonthdate[0] == "Tues":
			daystilwed = 1
		elif daymonthdate[0] == "Thur":
			daystilwed = 6
		elif daymonthdate[0] == "Fri":
			daystilwed = 5
		elif daymonthdate[0] == "Sat":
			daystilwed = 4
		elif daymonthdate[0] == "Sun":
			daystilwed = 3
	firstWed = int(daymonthdate[2]) + daystilwed

	secondWed = firstWed+7

	thirdWed = secondWed+7

	fourthWed = thirdWed+7

	wednesdays = [firstWed, secondWed, thirdWed, fourthWed]

	daystilfri = 0

	if daymonthdate[0] != "Fri":
		if daymonthdate[0] == "Wed":
			daystilfri = 2
		elif daymonthdate[0] == "Thur":
			daystilfri = 1
		elif daymonthdate[0] == "Sat":
			daystilfri = 6
		elif daymonthdate[0] == "Sun":
			daystilfri = 5
		elif daymonthdate[0] == "Mon":
			daystilfri = 4
		elif daymonthdate[0] == "Tues":
			daystilfri = 3
	firstfri = int(daymonthdate[2]) + daystilfri

	secondfri = firstfri+7

	thirdfri = secondfri+7

	fourthfri = thirdfri+7

	fridays = [firstfri, secondfri, thirdfri, fourthfri]

	print("Dates of Wednesdays this month: ", wednesdays)
	print("Dates of Fridays this month: ", fridays)
	print("Floors, bathrooms, and surfaces will need to be cleaned on: ", wednesdays[1], " and ", wednesdays[3])
	print("Clear out all old food from fridge on :", fridays[2])

	original_stdout = sys.stdout

	with open('amongus.txt', 'w') as f:
		sys.stdout = f
		print(wednesdays, "\n" , fridays)
		sys.stdout = original_stdout
if __name__ == '__main__':
	calBuild(day, date)