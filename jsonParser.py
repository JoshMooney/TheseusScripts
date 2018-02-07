#Python Parser

# Run this using 
#
# python jsonParser.py '{"name": "Josh"}'
#

import json
import sys

def is_valid(str):
	try:
		json_object = json.loads(str)
	except ValueError, e:
		return False, e
	return True, json_object

def prettY_format(value):
	if(value[0]):
		print json.dumps(value[1], sort_keys=True, indent=4, separators=(',', ': '))


var = sys.argv[1]
format(is_valid(var))
