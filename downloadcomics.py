import os
import requests
import bs4

url = "http://xkcd.com"
os.makedirs("xkcd", exist_ok=True) #store comics in ./xkcd
#download the web page
count = 0
while count < 12:
# while not url.endswith("#"):
    print("Downloading page %s..." % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html5lib")
#download pages with request module
    comicElem = soup.select("#comic img")
    if comicElem == []:
        print("could not find image")
    else:
        comicUrl = "http:" + comicElem[0].get("src")
        print("Downloading image %s..." %(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        imageFile = open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb")
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
    count = count + 1
print("done")
#download and save the comic image to the harddrive using iter_content

#find the url of the previous comic link and repeat
