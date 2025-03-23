import sys
import feedparser

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
    print(PodcastInfo(RSSxml, RSSurl))
    EpisodeInfo(RSSxml)
    GuestInfo()
    #print(podcast)
    #for i in range(len(RSSxml["items"])):
        #if RSSxml["items"][i]["itunes_episodetype"] != 'trailer':
            #print("NEW ITEM---")
            #print(RSSxml["items"][i])

def PodcastInfo(RSSxml, url):
    podcastdict = {}
    podcastdict["PodcastName"] = RSSxml.feed.title
    podcastdict["PodcastDescription"] = RSSxml.feed.subtitle
    podcastdict["PodcastLink"] = RSSxml.feed.link
    podcastdict["PodcastRSS"] = url
    return podcastdict

def EpisodeInfo(RSSxml):
    episodes = []
    #print(RSSxml["entries"])
    for i in range(len(RSSxml["entries"])):
        episodedict = {}
        #print(RSSxml.entries[i])
        episodedict["EpisodeName"] = RSSxml.entries[i].title
        episodedict["EpisodeDate"] = RSSxml.entries[i].published
        if "itunes_episode" in RSSxml.entries[i]:
            episodedict["EpisodeNumber"] = RSSxml.entries[i].itunes_episode
        else:
            episodedict["EpisodeNumber"] = ''
        if "link" in RSSxml.entries[i]:
            episodedict["EpisodeLink"] = RSSxml.entries[i].link
        else:
            episodedict["EpisodeLink"] = ''
        episodedict["EpisodeSummary"] = RSSxml.entries[i].description
        episodedict["EpisodeLength"] = RSSxml.entries[i].itunes_duration
        episodedict["EpisodeType"] = RSSxml.entries[i].itunes_episodetype
        episodes.append(episodedict)
    return episodes

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