import calenderbuilder
import emailwriter
import smtplib
import ssl


def main():
	
	port = 465 # For SSL
	smtp_server = "smtp.gmail.com"
	day = "Mon"
	date = "1"
	sender_email = "dkf55@nau.edu"
	password = "HaHaHay0uThoughtIwouldactuallyputmYem@ilhere,FOOL"
	emails = ["5552698655@vtext.com","5558851652@vtext.com","5554216978@vtext.com","5553360383@txt.att.net"]

	calenderbuilder.calBuild(day, date)
	emailwriter.sussyBaka()

	messages = []

	f = open("sussybaka.txt", 'r')

	message = f.read()

	f.close()
		
	print(message)


	# Create a secure SSL context
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, emails[0], message) #sends the email


