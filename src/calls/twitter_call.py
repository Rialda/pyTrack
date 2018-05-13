import filemapper as fm
import pandas as pd
import glob
import json, codecs, csv
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.TweetScraper
collection = db.tweet

december = db.december
january = db.january
february = db.february
march = db.march
april = db.april

#fileToWriteInto="C:/Users/Rialda/PycharmProjects/pyTrack/src/TweetScrap/TweetScraper/TweetScraper/Data/data.csv"
#writing = open(fileToWriteInto, 'a')


def twitter_api():
    dictlist = []
  #  for doc in april.find({}, no_cursor_timeout=True):
   #     dictlist.append(doc)
    #    df = pd.DataFrame(dictlist)
    #    df = df.replace({'\n': ' '}, regex=True)  # remove linebreaks in the dataframe
    #    df = df.replace({'\t': ' '}, regex=True)  # remove tabs in the dataframe
    #    df = df.replace({'\r': ' '}, regex=True)  # remove carriage return in the dataframe
    #    df.to_csv("C:/Users/Rialda/PycharmProjects/pyTrack/src/TweetScrap/TweetScraper/TweetScraper/Data/april.csv")
    #    print(doc)
    print("Done!")
    #collection.cursor.close()
    return "done"


#files = glob.glob('C:/Users/Rialda/PycharmProjects/pyTrack/src/TweetScrap/TweetScraper/TweetScraper/Data/twets/*')
#len(files)
#dictlist = []
#for file in files:
 #   json_string = open(file, 'r').read()
  #  json_dict = json.loads(json_string)
   # dictlist.append(json_dict)
   # df = pd.DataFrame(dictlist)
    #df = df.replace({'\n': ' '}, regex=True)  # remove linebreaks in the dataframe
    #df = df.replace({'\t': ' '}, regex=True)  # remove tabs in the dataframe
    #df = df.replace({'\r': ' '}, regex=True)  # remove carriage return in the dataframe
    #df.to_csv("C:/Users/Rialda/PycharmProjects/pyTrack/src/TweetScrap/TweetScraper/TweetScraper/Data/data.csv")