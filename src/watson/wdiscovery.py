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


testphrase = 'I am catching a flu now. This is plain awful, I feel terrible!!'


response = natural_language_understanding.analyze(
    text="something about some stuff",
    features=Features(
        entities=EntitiesOptions(
            emotion=True,
            sentiment=True,
            limit=5),
        keywords=KeywordsOptions(
            emotion=True,
            sentiment=True,
            limit=5)))
print(json.dumps(response, indent=2))

response2 = natural_language_understanding.analyze(
    text=testphrase,
    features=Features(entities=EntitiesOptions(), keywords=KeywordsOptions(),
                      categories=CategoriesOptions(), concepts=ConceptsOptions())
)
aaa = (json.dumps(response2, indent=2))
print(aaa)
bbb = json.loads(aaa)
single_thing = str(bbb['usage']['text_characters'])


def nlu():
    testphrase2 = 'I am catching a flu now. This is plain awful, I feel terrible!!'
    response2 = natural_language_understanding.analyze(
        text=testphrase2,
        features=Features(entities=EntitiesOptions(), keywords=KeywordsOptions(),
                          categories=CategoriesOptions(), concepts=ConceptsOptions())
        )
    aaa = (json.dumps(response2, indent=2))
    print (aaa)
    bbb = json.loads(aaa)
    single_thing = str(str(bbb['categories']))
    nlu2(single_thing)

    response3 = natural_language_understanding.analyze(
        url='https://newsapi.org/v2/everything?q=influenza&sortBy=publishedAt&apiKey=4f3a2f68ac6c4de88cda6999cd7c25a9',
        features=Features(
            categories=CategoriesOptions(),
            concepts=ConceptsOptions(limit=3)))

    print(json.dumps(response3, indent=2))
    return response2


def nlu2(the_result):
    f = open("C:/Users/Rialda/PycharmProjects/pyTrack/src/watson/writingfile.txt", 'a')
    f.write(the_result+'\n')


