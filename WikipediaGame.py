import requests
import bs4
from random import randint
from time import sleep


def PlayWikipediaGame():
    url = input("Enter a valid wikipedia URL: ")
    def getURL(url):
        while True:
            if ("wikipedia.org/wiki/" in url.lower()):
                return url
            url = input("Enter a valid wikipedia URL: ")
    url = getURL(url)
    while True:
        try:
            initialArticle = requests.get(url)
            assert "wikipedia.org/wiki/" in url.lower()
            break
        except:
            url=""
            getURL(url)
    articles=[]
    soup = bs4.BeautifulSoup(initialArticle.content, "lxml")
    try:
        articles.append(soup.find("span",class_="mw-page-title-main").text)
    except:
        articles.append(url)
    while True:
        try:
            times = int(input("How many links?: "))
            assert times>1
            break
        except:
            print("Must be over 1 link")
    for i in range(times):
        linkList = soup.findAll('a', href=True)
        chosenLink = linkList[randint(0,len(soup))]['href']
        while "/wiki/" not in chosenLink or chosenLink in ("/wiki/Main_Page","/wiki/Wikipedia:Contents") or ":" in chosenLink or "#" in chosenLink:
            chosenLink = linkList[randint(0, len(linkList)-1)]['href']
        if ('https://' not in chosenLink and 'wikipedia.com' not in chosenLink):
            chosenLink="https://en.wikipedia.com"+chosenLink
        newLink = requests.get(chosenLink)
        soup = bs4.BeautifulSoup(newLink.content, "lxml")
        thingy = soup.find(class_="mw-page-title-main")
        try:
            assert type(thingy.text)==type("gergergerg")
            articles.append(str(thingy.text))
        except:
            articles.append(newLink)
    print("\n")
    print(f"Get from {articles[0]} to {articles[-1]} in under {times} links")
    sleep(3)
    input("Press enter to reveal path")
    print(" -> ".join(articles))
    if (input("Play again? (Y/N): ").lower()=='y'):
        PlayWikipediaGame()
    else:
        return



PlayWikipediaGame()