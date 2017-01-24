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
	
	class_ids = []
	class_names = []

	for i in xrange(item_count):
		class_ids.append(jsond["sv_extras"]["sx_courses"][i]["id"])
		class_names.append(jsond["sv_extras"]["sx_courses"][i]["name"])
			
	return {"ids": class_ids, "names": class_names}
