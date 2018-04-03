from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, CategoriesOptions, ConceptsOptions


natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='ceeee187-8086-4249-ac2d-349d397d05a7',
  password='obhjatmRAiQy',
  version='2018-03-16')

def discover():
    response = natural_language_understanding.analyze(
      text='The plan is part of a concerted drive to move top artworks out of Parisian museums and around the country in doing so break down the “cultural segregation” with deprived areas.',
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
        text='However, the minister was said to be reconsidering moving the Leonardo Da Vinci’s 16th century masterpiece after being shown an estimation of the costs of the move.',
        features=Features(entities=EntitiesOptions(), keywords=KeywordsOptions()))

    print(json.dumps(response2, indent=2))
    response3 = natural_language_understanding.analyze(
      url='https://www.telegraph.co.uk/news/2018/04/03/proposed-mona-lisa-grand-tour-france-could-cost-30m-warns-louvre/',
      features=Features(
        categories=CategoriesOptions(),
      concepts=ConceptsOptions(limit=3)))

    print(json.dumps(response3, indent=2))
    return response3
