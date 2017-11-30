import requests
import json
#import os
#cwd = os.getcwd()
#print (cwd)

head= {"Accept": "applicaiton/json"}
f = open('bookies/api_key.txt', 'r')
api_key = f.read() 
f.close()

api_url = "https://api.the-odds-api.com/v2/odds/?apiKey=" + api_key
sports_url = "https://api.the-odds-api.com/v2/sports/?apiKey=" + api_key

def get_soccer_leagues():
	soccer_list = []
	ret = requests.get(sports_url,headers=head)
	
	sports_list = ret.json()['data']
	for sport in sports_list:
		if "Soccer" in sport['sport_group']:
			soccer_list.append(sport)

	return {"result":soccer_list}

def get_odds(sport, region):
	url = api_url+ "&sport=" + sport + "&region=" + region
	ret = requests.get(url,headers=head)
	return ret.json()

#print (get_soccer_leagues())


#sport = "NBA"
#region = "au"

#
#print (ret1.content)

#print (json.dumps(ret.json(), indent=2))

