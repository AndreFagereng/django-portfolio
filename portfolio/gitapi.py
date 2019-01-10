import requests
import json

'''
Simple get request which returns selected data for view.
No need to API token.
'''
def get_response(url):
	return requests.get(url)

def list_view(data):
	data = [{'name':r['name'],
			'full_name':r['full_name'],
			'html_url':r['html_url'],
			'description':r['description'],
			'language':r['language']} 
			for r in json.loads(data.text)]
	return data

