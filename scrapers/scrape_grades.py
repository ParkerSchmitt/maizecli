from lxml import html
from pprint import pprint
import json

def scrape(session):
	## scrape stuff

	url = "https://maize.blackboard.com/webapps/streamViewer/streamViewer"
	page = session.get('https://maize.blackboard.com/webapps/streamViewer/streamViewer')

	payload = {
	"cmd": "loadStream",
	"streamName": "mygrades",
	"providers": "%7B%7D",
	"forOverview": "false"}
	result = session.post(url, data=payload, headers=dict(referer=url))
	
	jsond = json.loads(result.text)
	
	# Get the amount of grades/classes there are.
	item_count = len(jsond["sv_extras"]["sx_courses"])
	
	grades = []
	classes = []
	
	# Create two loops to allow us to compare each grade to the class
	for x in xrange(item_count):
		for y in xrange(item_count):
			## Check to see if both of the ids match (the json data is submitted out of order, so we have to order them), and make sure that the grade is not nothing, which would mean that the class has not begun.
			if jsond["sv_extras"]["sx_courses"][x]["id"] == jsond["sv_streamEntries"][y]["se_courseId"] and jsond["sv_streamEntries"][y]["itemSpecificData"]["gradeDetails"]["displayGradeGrade"] != None:
				
				classes.append(jsond["sv_extras"]["sx_courses"][x]["name"])
				grades.append(jsond["sv_streamEntries"][y]["itemSpecificData"]["gradeDetails"]["displayGradeGrade"])
	
	return {"grades": grades, "classes": classes}
