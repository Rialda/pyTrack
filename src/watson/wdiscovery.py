from __future__ import print_function
import json, csv
from watson_developer_cloud import NaturalLanguageUnderstandingV1, DiscoveryV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, CategoriesOptions, ConceptsOptions


natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='ceeee187-8086-4249-ac2d-349d397d05a7',
  password='obhjatmRAiQy',
  version='2018-03-16')

#discovery = DiscoveryV1(
 #   version='2017-11-07',
  #  username='f00dc7e6-1305-4c0d-b0a4-eb113393a9c9',
   # password='yr1OkyPUdNje')
#
#environments = discovery.list_environments()
#print(json.dumps(environments, indent=2))


def discover():
    return "todo"


fileToRead="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/testfile.xlsx"
fileToWrite="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/outCategories.csv"
filetoFeel="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/keywordsSentimentEmotions.csv"


def nlu():
    #g = open(fileToWrite, 'a')
    e = open(filetoFeel, 'a')
    f = open(fileToRead, 'r')
    num_lines = sum(1 for line in open(fileToRead))
    while num_lines!=0:
        nline=f.readline()
        newline = str(nline)
        if len(newline)>15:
            response2 = natural_language_understanding.analyze(
            text=newline,
            language='en',
            features=Features(keywords=KeywordsOptions(emotion=True, sentiment=True, limit=2))
            )
            aaa = (json.dumps(response2, indent=2))
            print(aaa)
            bbb = json.loads(aaa)
           # single_thing = (str(bbb['categories']))
            single_sentiment = (str(bbb['keywords']))
           # g.write(single_thing+'\n')
            e.write(single_sentiment+'\n')
        else:
            #g.write("Not enough data"+'\n')
            e.write("Not enough data"+'\n')
        num_lines-=1
    return num_lines


def nlu2(the_result):
    f = open("C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/writingfile.txt", 'a')
    f.write(the_result+'\n')


