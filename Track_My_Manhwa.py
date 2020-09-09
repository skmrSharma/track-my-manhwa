#! python3
# add more manga to the below list with their url
# works only for Patreon group translations
import requests, bs4
mangaDict = {"Dimensional Mercenary": "https://reaperscans.com/comics/58193-dimensional-mercenary", "The Descent of the Demonic Master": "https://leviatanscans.com/comics/866673-the-descent-of-the-demonic-master", "Survival Story of a Sword King in a Fantasy World": "https://leviatanscans.com/comics/11268-survival-story-of-a-sword-king-in-a-fantasy-world", "My Dad is too Strong": "https://leviatanscans.com/comics/956629-my-dad-is-too-strong/"}
for mangaName,mangaURL in mangaDict.items():
    res = requests.get(mangaURL)
    if res.status_code == requests.codes.ok:
        lastUpdatedElem = bs4.BeautifulSoup(res.text, "lxml").select("div .item-date")
        print(mangaName + ": " + lastUpdatedElem[0].getText())
    else:
        print("Error: Url for " + mangaName + " was not found !")
        continue