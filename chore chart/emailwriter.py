import sys

# read dates from amongus.txt
# compose emails to send to idiot
# write emails to sussybaka.txt

def sussyBaka():

	f = open("amongus.txt", "r")

	wednesdaysText = f.readline()
	fridaysText = f.readline()

	f.close()

	wednesdaysText = wednesdaysText.replace('[', '')
	wednesdaysText = wednesdaysText.replace(']','')
	wednesdaysText = wednesdaysText.replace(',', '')

	wednesdaysText = wednesdaysText.strip()

	fridaysText = fridaysText.replace('[', '')
	fridaysText = fridaysText.replace(']','')
	fridaysText = fridaysText.replace(',', '')

	fridaysText = fridaysText.strip()

	wednesdays = wednesdaysText.split(" ")
	fridays = fridaysText.split(" ")


	f = open("sussybaka.txt", 'w')
	f.write("""If you are receiving this message, it is because you have been selected for the following chores this month:
Trash and Recycling every Wedesday/Sunday, and Dishes every Monday/Wednesday/Friday.

sussybaka

If you are receiving this message, it is because you have been selected for the following chores this month:
Sweeping/Vacuuming all public areas twice. It is expected you will complete these tasks by/on the following Wednesdays: """ + wednesdays[1] +", " + wednesdays[3] + """
Please note these are the same days required as the other chores if you want to wait to do a group cleaning session and feel more motivated or something idk.

sussybaka

If you are receiving this message, it is because you have been selected for the following chores this month:
Dusting/Cleaning all surfaces in public areas (fans, tables, counters, etc). It is expected you will complete these tasks by/on the following Wednesdays: """+ wednesdays[0]+", " + wednesdays[1] +", " + wednesdays[2] + ", and" + wednesdays[3] + """

sussybaka

If you are receiving this message, it is because you have been selected for the following chores this month:
Cleaning two restrooms (Billy just clean the downstairs one). It is expected you will complete these tasks by/on the following Wednesdays: """+ wednesdays[1] + ", " + wednesdays[3]+"""
Please note these are the same days required as the other chores if you want to wait to do a group cleaning session and feel more motivated or something idk.

sussybaka

This message is for everyone to remind them that the 3rd Friday of this month, on the """+ fridays[2] + """ will be the day everyone is to go through the fridge/freezer and toss any leftovers/spoiled goods.""")
	f.close()

if __name__ == '__main__': 
	sussyBaka()

#dishes = mon, wed, fri -----done
#floors, bathrooms, surfaces = 2nd(at most 14th)/4th(at most 28th) wed ---done
#trash, recycling = wed, sun ---done
#refrigerator = 3rd fri ---done