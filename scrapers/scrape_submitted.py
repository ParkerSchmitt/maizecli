from lxml import html
from pprint import pprint
import json
import scrape_class_data

def scrape(session):
	## scrape stuff

	
	class_data = scrape_class_data.scrape(session)
	
	upcoming_assignments = {}	
	for i in xrange(len(class_data["ids"])):
		page = session.get("https://maize.blackboard.com/webapps/bb-mygrades-BBLEARN/myGrades?course_id=%s&stream_name=mygrades#" % class_data["ids"][i])
		tree = html.fromstring(page.text)
		upcoming_names = tree.xpath("//div[contains(@class, 'upcoming_item_row')]/div[@class='cell gradable']/text()[1]")
		upcoming_dates = tree.xpath("//div[contains(@class, 'upcoming_item_row')]/@duedate")
		res = upcoming_names
		upcoming_names = [upcoming_names for upcoming_names in (upcoming_names.strip() for upcoming_names in res) if upcoming_names]
		upcoming_data = {"name": upcoming_names, "date": upcoming_dates}
		upcoming_assignments[class_data["names"][i]] = upcoming_data


	return upcoming_assignments


