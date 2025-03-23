import sys
import feedparser
import time

def main():
    arguments = sys.argv
    if len(arguments) != 2:
        print("Please provide a single RSS feed only.")
        exit()
    RSSurl = arguments[1]
    RSSxml = feedparser.parse(RSSurl)
    if RSSxml['bozo'] == 1:
        print("Please provide a valid RSS feed")
        exit()
    PodcastSQLCreation(PodcastInfo(RSSxml, RSSurl), EpisodeInfo(RSSxml))
    GuestInfo()

def PodcastInfo(RSSxml, url):
    podcastdict = {}
    fields = [("title","PodcastName"),("summary","PodcastDescription"),("link","PodcastLink")]
    for value in fields:
            podcastdict[value[1]] = RSSxml.feed[value[0]] if value[0] in RSSxml.feed else ''
    podcastdict["PodcastRSS"] = url
    #print(podcastdict)
    return podcastdict

def EpisodeInfo(RSSxml):
    episodes = []
    #print(RSSxml["entries"])
    fields = [("title","EpisodeName"),("published_parsed","EpisodeDate"),("itunes_episode","EpisodeNumber"),("link","EpisodeLink"),("description","EpisodeSummary"),("itunes_duration","EpisodeLength"),("itunes_episodetype","EpisodeType")]
    for i in range(len(RSSxml["entries"])):
        episodedict = {}
        #print(RSSxml.entries[i])
        for value in fields:
            episodedict[value[1]] = RSSxml.entries[i][value[0]] if value[0] in RSSxml.entries[i] else ''
        episodes.append(episodedict)
        episodedict["EpisodeDate"] = time.strftime('%m-%d-%Y',episodedict["EpisodeDate"])
    return episodes

def PodcastSQLCreation(podcast, episodes):
    podcastnbr = 1
    #podcast columns
    columns = ["PodcastName","PodcastDescription","PodcastLink","PodcastRSS"]
    podcastSQL = f"INSERT INTO podcastproject.podcast\nVALUES ({podcastnbr}, "
    for col in columns:
        podcast[col] = podcast[col].replace("'","''")
        podcastSQL = podcastSQL + "'" + str(podcast[col][:255] + "', ")
    podcastSQL = podcastSQL + "CURRENT_TIMESTAMP());"
    print(podcastSQL)
    columns = ["EpisodeName","EpisodeDate","EpisodeLink","EpisodeSummary","EpisodeLength"]
    episodenbr = 1
    episodeSQL = ""
    for ep in reversed(episodes):
        if episodenbr != 1:
            episodeSQL = episodeSQL + "\n\n"
        episodeSQL = episodeSQL + f"INSERT INTO podcastproject.podcastepisode\nVALUES ({podcastnbr}, {episodenbr}, "
        for col in columns:
            ep[col] = ep[col].replace("'","''")
            ep[col] = ep[col].replace("\n"," ")
            if col == "EpisodeDate":
                episodeSQL = episodeSQL + 'STR_TO_DATE("' + ep["EpisodeDate"] + '", "%m-%d-%Y"), '
            else:
                episodeSQL = episodeSQL + "'" + str(ep[col][:255]) + "', "
        episodeSQL = episodeSQL + "CURRENT_TIMESTAMP());"
        episodenbr += 1
    print(episodeSQL)
    #print(episodes)
    return

def GuestInfo():
    guestlist = ['Abby Cox',
        'Abigail Thorn',
        'Adam Chase ',
        'Adam Ragusea',
        'Adam Savage',
        'Alec Steele',
        'Alec Watson',
        'Ali Spagnola',
        'Amelie Brodeur',
        'Andrew Hunter Murray',
        'Anna Ploszajski',
        'Anna Ptaszynski',
        'Annie Rauwerda',
        'Ashley Hamer',
        'Bec Hill',
        'Becky Stern',
        'Ben Doyle',
        'Bernadette Banner',
        'Beryl Shereshewsky',
        'Bill Sunderland',
        'Bob Hagh',
        'Brady Haran',
        'Brian David Gilbert',
        'Brian McManus',
        'Caroline Roper',
        'Carson Woody',
        'Ceri Riley',
        'Cleo Abram',
        'Corry Will',
        'Dan Schreiber',
        'Dani Siller',
        'Daniel Peake',
        'David Bennett',
        'Eglė Vaškevičiūtė',
        'Ella Hubber',
        'Emily Calandrelli',
        'Emily Graslie',
        'Emily the Engineer',
        'Eric Johnson',
        'Estefannie',
        'Evan Edinger',
        'Evan Heling',
        'Francis Heaney',
        'Geoff Marshall',
        'Grady Hillhouse',
        'Hank Green',
        'Hannah Crosbie',
        'Hannah Fry',
        'Hannah Witton',
        'Hayley Loren',
        'Inés Dawson',
        'Iszi Lawrence',
        'J. Draper',
        'Jabrils',
        'Jack Chesher',
        'Jacklyn Dallas',
        'Jade Tan-Holmes',
        'James Harkin',
        'Jarvis Johnson',
        'Jason Slaughter',
        'Jay Foreman',
        'Jenny Draper',
        'Jeremy Fielding',
        'Joe Hanson',
        'Jordan Adika',
        'Jordan Harrod',
        'Julian Huguet',
        'Julian O\'Shea',
        'Karen Chu',
        'Karen Kavett',
        'Katelyn Heling',
        'Katie Steckles',
        'Kip Heath',
        'Devin Stone',
        'Lily Hevesh',
        'Lizzy Skrzypiec',
        'Lucy Rogers',
        'Luke Cutforth',
        'Mark Rober',
        'Marques Brownlee',
        'Mary Spender',
        'Matt Gray',
        'Matt Parker',
        'Matthew Schuchman',
        'Mehdi Sadaghdar',
        'Melissa Fernandes',
        'Michelle Khare',
        'Mike Boyd',
        'Molly Edwards',
        'Nahre Sol',
        'Nicholas Johnson',
        'Ólafur Waage',
        'Rebecca Smethurst',
        'Robert Llewellyn',
        'Rowan Ellis',
        'Ruth Amos',
        'Sabrina Cruz',
        'Sam Denby',
        'Sam Meeps',
        'Sam Reich',
        'Sarah Renae Clark',
        'Scott Manley',
        'Shawn Brown',
        'Simon Clark',
        'Simone Giertz',
        'Sophie Ward',
        'Stuart Ashen',
        'Stuart Goldsmith',
        'AhmedMia',
        'Taha Khan',
        'Tina Huang',
        'Toby Hendy',
        'Tom Crawford',
        'Tom Lum',
        'Trace Dominguez',
        'Vanessa Hill',
        'Virginia Schutte',
        'William Osman',
        'Wren Weichman',
        'Xyla Foxlin']
    

if __name__ == "__main__":
    main()