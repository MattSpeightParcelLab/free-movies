import requests
import re
import pprint
import os

""" https://123movies00.org/genre/ """
"""
GET /movie/search/transporter HTTP/1.1
"""


def watchFilm(): #By Name
	searchTerm = raw_input("Film Name: ") # Update code for python3
	headers={"Host":"123movies00.org","User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language":"en-GB,en;q=0.5","Accept-Encoding":"gzip, deflate","Connection":"close","Cookie":"__test; noShowWelcome=true; __test; __cfduid=d406039e696df40844f87a00d7e8453191558888545; __atuvc=4%7C22; __atuvs=5ceac062b397b565003; _ga=GA1.2.1128633050.1558888547; _gid=GA1.2.2048887501.1558888547; subscribe=1; PHPSESSID=kanhb6f5ddcr5e7rs0q02n1ig7; AdskeeperStorage=%7B%220%22%3A%7B%22svspr%22%3A%22https%3A%2F%2F123movies00.org%2Fmovie%2Fsearch%2Ftransporter%22%2C%22svsds%22%3A1%2C%22TejndEEDj%22%3A%22TyvYeYhpV%22%7D%2C%22C344312%22%3A%7B%22page%22%3A1%2C%22time%22%3A1558888562274%7D%7D","Upgrade-Insecure-Requests":"1"}
	#cookies = {"__test":"","noShowWelcome":"true","__test":"","__cfduid":"d406039e696df40844f87a00d7e8453191558888545","__atuvc":"3%7C22","__atuvs":"5ceac062b397b565002","_ga":"GA1.2.1128633050.1558888547","_gid":"GA1.2.2048887501.1558888547","subscribe":"1","PHPSESSID":"kanhb6f5ddcr5e7rs0q02n1ig7","AdskeeperStorage":"%7B%220%22%3A%7B%22svspr%22%3A%22https%3A%2F%2F123movies00.org%2Fmovie%2Fsearch%2Ftransporter%22%2C%22svsds%22%3A1%2C%22TejndEEDj%22%3A%22TyvYeYhpV%22%7D%2C%22C344312%22%3A%7B%22page%22%3A1%2C%22time%22%3A1558888562274%7D%7D"}
	r = requests.post("https://123movies00.org/movie/search/"+searchTerm, headers=headers).text

	tempurls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r)

	urls = []

	for url in tempurls:

		url = url.encode('ascii','ignore').lower()
		if searchTerm in url:
			if "https://123movies00.org/movie/" in url:
				if ".html" in url:
					urls.append(url)

	
	getVid(urls)




def getVid(movieList): # MovieList Array
	#Choose Film

	movieNames = []

	for movie in movieList:

		movie = find(movie, ["e", "1"])
		movie = find(movie, ["e", "1"])
		movie = find(movie, ["/", "/"])
		movie = find(movie, ["/", "/"])

		movieNames.append(movie)

		#movieNames.append(find(find(find(find(movie, ["e", "1"]), ["e", "1"]), ["\/", "\/"]), ["\/", "\/"])) # get video id

	for x in range(len(movieList)):
		print(str(x+1)+" - "+ movieNames[x])

	movieId = int(raw_input("Which film to watch: (0-"+str(len(movieList))+")"))-1
	movieurl = movieList[movieId]
	
	headers={"Host":"123movies00.org","User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language":"en-GB,en;q=0.5","Accept-Encoding":"gzip, deflate","Connection":"close","Cookie":"__test; noShowWelcome=true; __test; __cfduid=d406039e696df40844f87a00d7e8453191558888545; __atuvc=4%7C22; __atuvs=5ceac062b397b565003; _ga=GA1.2.1128633050.1558888547; _gid=GA1.2.2048887501.1558888547; subscribe=1; PHPSESSID=kanhb6f5ddcr5e7rs0q02n1ig7; AdskeeperStorage=%7B%220%22%3A%7B%22svspr%22%3A%22https%3A%2F%2F123movies00.org%2Fmovie%2Fsearch%2Ftransporter%22%2C%22svsds%22%3A1%2C%22TejndEEDj%22%3A%22TyvYeYhpV%22%7D%2C%22C344312%22%3A%7B%22page%22%3A1%2C%22time%22%3A1558888562274%7D%7D","Upgrade-Insecure-Requests":"1"}
	#cookies = {"__test":"","noShowWelcome":"true","__test":"","__cfduid":"d406039e696df40844f87a00d7e8453191558888545","__atuvc":"3%7C22","__atuvs":"5ceac062b397b565002","_ga":"GA1.2.1128633050.1558888547","_gid":"GA1.2.2048887501.1558888547","subscribe":"1","PHPSESSID":"kanhb6f5ddcr5e7rs0q02n1ig7","AdskeeperStorage":"%7B%220%22%3A%7B%22svspr%22%3A%22https%3A%2F%2F123movies00.org%2Fmovie%2Fsearch%2Ftransporter%22%2C%22svsds%22%3A1%2C%22TejndEEDj%22%3A%22TyvYeYhpV%22%7D%2C%22C344312%22%3A%7B%22page%22%3A1%2C%22time%22%3A1558888562274%7D%7D"}
	r = requests.post(movieurl, headers=headers).text.splitlines()

	id = find(find(search(r, 'data-openload="'), ["d", " "]), ["\"", "\""]) # get video id


	os.system("chromium-browser \"https://openload.co/embed/"+id+"\"") # Change "firefox" based on browser



	# Search
def search(txt, searchvar):
    for line in txt:
        if re.search(searchvar, line, re.I):
            return line


# Find a value between two chars - first result
def find(txt, var):
    text = ""


    arr = list(txt)

    count = 0

    for a in arr:
        if a == var[0]:
            arr = arr[count + 1:len(arr) - 1]
            break
        count += 1

    count = 0

    for a in arr:
        if a == var[1]:
            arr = arr[0:count]
            break
        count += 1

    text = ''.join(arr)
    return text

 

watchFilm()




