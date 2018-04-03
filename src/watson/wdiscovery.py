from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, CategoriesOptions


natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='ceeee187-8086-4249-ac2d-349d397d05a7',
  password='obhjatmRAiQy',
  version='2018-03-16')

def discover():
    response = natural_language_understanding.analyze(
      text='IBM is an American multinational technology company '
           'headquartered in Armonk, New York, United States, '
           'with operations in over 170 countries.',
      features=Features(
        entities=EntitiesOptions(
          emotion=True,
          sentiment=True,
          limit=2),
        keywords=KeywordsOptions(
          emotion=True,
          sentiment=True,
          limit=2)))
    print(json.dumps(response, indent=2))
    response2 = natural_language_understanding.analyze(
        text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
             'Superman fears not Banner, but Wayne.',
        features=Features(entities=EntitiesOptions(), keywords=KeywordsOptions()))

    print(json.dumps(response2, indent=2))
    response3 = natural_language_understanding.analyze(
      url='www.ibm.com',
      features=Features(
        categories=CategoriesOptions()))

    print(json.dumps(response3, indent=2))
