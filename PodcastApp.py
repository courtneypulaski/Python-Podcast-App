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
    print(len(RSSxml))
    #print(RSSxml["items"])
    for i in range(len(RSSxml["items"])):
        if RSSxml["items"][i]["itunes_episodetype"] != 'trailer':
            print("NEW ITEM---")
            print(RSSxml["items"][i])
    #print(len(RSSxml["items"]))

if __name__ == "__main__":
    main()