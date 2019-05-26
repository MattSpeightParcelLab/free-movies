import requests
import re

""" https://123movies00.org/genre/ """


def getML(): #By Name
	searchTerm = input("Film Name: ")
	r = requests.get("https://123movies00.org/movie/search/"+searchTerm).text

	urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', r)

	return 

