import os
import click
import json
import requests
from lxml import html
import scrapers
import time

session_requests = requests.session()


"""
Tries to log into the Blackboard in site with inputted credentials. If it can successfully log in, it returns true, if it can't, it returns false.

parameters:
	cred LIST [username, password] -- the credentials to POST to the server.
"""
def login_test(cred):
	## web scrape url, input username password, see if it works.

	payload = {
	"user_id": cred[0], 
	"password": cred[1], 
	}
	

	login_url = "https://maize.blackboard.com/webapps/login/"
	result = session_requests.get(login_url)

	result = session_requests.post(
 	login_url, 
 	data = payload, 
 	headers = dict(referer=login_url)
	)
	
	## if works, return session, if doenst, return false
	if result.url != login_url:
		return True
	else:
		return False
	
"""
Function that runs first time program is used/if usr.dat file is missing. Checks to see if they inputted working username and password, and if so saves it in usr.dat

parameters:
	username STRING -- username to try
	password STRING -- password to try

"""
@click.command()
@click.option("--username", prompt="Username")
@click.option("--password", prompt="Password", hide_input=True)
def login(username,password):
	click.echo("Checking login...")
	
	login_success = login_test([username,password])
	
	if login_success:
		user_data = [username,password]
		with open('usr.dat', 'w') as file:
			json.dump(user_data,file)
		print ("login successful. saving credentials")
	else:
		click.echo("login failed. please try again.")
		

"""
Function that enables the Click libary to store other command line functions under a group
"""
@click.group()
def cli():
	pass
		

"""
Command line function to allow users to check various information in blackboard.

parameters: 
	option STRING (grades,submitted,analytics) -- tells the function what to check for
	weeks STRING/INT -- tells the submitted function how many weeks to look for unsubmitted work for
"""
@cli.command()
@click.option("--grades", "option", flag_value="grades", default=True, help="displays your current grade average in Blackboard")
@click.option("--submitted", "option", flag_value="submitted", help="displays unsubmitted assignments in Blackboard")
@click.option("--analytics", "option", flag_value="analytics", help="displays analytical information (average time to complete assignment, average grade, projected grades)")
@click.option("--weeks", "weeks", default="7", help="displays amount of weeks to look for data. only avaliable for the --submitted flag")
def check(option,weeks):
	click.echo("Checking %s" % option)	
	
	if option == "grades":
		data = scrapers.scrape_grades.scrape(session_requests)
		click.echo("GRADE | CLASS")	
		for i in xrange(len(data["classes"])):
			click.echo("%s | %s" % (data["grades"][i], data["classes"][i]))
			
	elif option == "submitted":
		data = scrapers.scrape_submitted.scrape(session_requests)
		click.echo("the following assignments are upcoming:")
		click.echo("ASSIGMENT | CLASS|")
		for class_name in data:
			for y in xrange(len(data[class_name]["name"])):
				if int(data[class_name]["date"][y]) <= int(time.time()*1000) * 1 * int(weeks) and int(data[class_name]["date"][y]) > int(time.time()*1000): # Check to see if the time on the assignment minus the current time is greater than a a chosem amount of days. if it is, than we don't have to worry about it/ Also make sure that the due date is not greater than the current date, which would mean it is to late to do it.	
					click.echo("%s | %s" % (data[class_name]["name"][y], class_name))

					

"""
Main function, called when program first starts. Before doing anything else, checks to see if the user is logged in, if the user isn't, it forces them to log in. If
the user is logged in however, it calls cli, enabling the user to use all the functions under the cli group.
"""
def main():
	## Logining in is required to use this program. Make sure that the user a) has made a attempt to login previously,and that the login actually works.
	if os.path.isfile("usr.dat"):
		with open('usr.dat', 'r') as file:
			data = json.load(file)
		if login_test(data):
			pass
		else:
			login()
			return
	else:
		login()
		return
	
	## If none of the above was false and returned, then we know we can allow the program to use all commands under the group "cli"
	cli()
	
	
if __name__ == '__main__':
	main()
