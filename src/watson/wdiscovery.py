from __future__ import print_function
import json, csv
from watson_developer_cloud import NaturalLanguageUnderstandingV1, DiscoveryV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, CategoriesOptions, ConceptsOptions


natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='17c67ee5-0175-4642-901e-aa734979890b',
  password='hanNZ7QZVrvv',
  version='2018-03-16')

#discovery = DiscoveryV1(
 #   version='2017-11-07',
  #  username='f00dc7e6-1305-4c0d-b0a4-eb113393a9c9',
   # password='yr1OkyPUdNje')
#
#environments = discovery.list_environments()
#print(json.dumps(environments, indent=2))


def discover():
    return "Discovery"


fileToRead="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/filewithdata.txt"
fileToWrite="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/fileforoutputdata.txt"
filetoFeel="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/fileforoutputdata2.txt"

#input tweets
november_tweets="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/input_tweets/november_tweets.txt"
december_tweets="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/input_tweets/december_tweets.txt"
january_tweets="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/input_tweets/january_tweets.txt"
february_tweets="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/input_tweets/february_tweets.txt"
march_tweets="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/input_tweets/march_tweets.txt"
april_tweets="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/input_tweets/april_tweets.txt"

#output ground truth
november_gt="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/output_gt/november_gt.txt"
december_gt="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/output_gt/december_gt.txt"
january_gt="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/output_gt/january_gt.txt"
february_gt="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/output_gt/february_gt.txt"
march_gt="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/output_gt/march_gt.txt"
april_gt="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/output_gt/april_gt.txt"

#output sentiment and emotion
november_opinion="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/output_opinion/november_opinion.txt"
december_opinion="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/output_opinion/december_opinion.txt"
january_opinion="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/output_opinion/january_opinion.txt"
february_opinion="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/output_opinion/february_opinion.txt"
march_opinion="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/output_opinion/march_opinion.txt"
april_opinion="C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/months/output_opinion/april_opinion.txt"


def nlu():
    f = open(november_tweets, 'r', encoding='UTF8')
    g = open(november_gt, 'a')
    e = open(november_opinion, 'a')
    num_lines = sum(1 for line in open(november_tweets, encoding='UTF8'))
    while num_lines!=0:
        nline=f.readline()
        newline = str(nline)
        if len(newline)>15:
            response2 = natural_language_understanding.analyze(
            text=newline,
            language='en',
            features=Features(keywords=KeywordsOptions(emotion=True, sentiment=True, limit=2), categories=CategoriesOptions())
            )
            aaa = (json.dumps(response2, indent=2))
            print(aaa)
            bbb = json.loads(aaa)
            single_thing = (str(bbb['categories']))
            single_sentiment = (str(bbb['keywords']))
            g.write(single_thing+'\n')
            e.write(single_sentiment+'\n')
        else:
            g.write("Not enough data"+'\n')
            e.write("Not enough data"+'\n')
        num_lines-=1
    return num_lines


def nlu2(the_result):
    f = open("C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/writingfile.txt", 'a')
    f.write(the_result+'\n')


