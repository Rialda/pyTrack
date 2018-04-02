from __future__ import print_function
import json
from watson_developer_cloud import DiscoveryV1
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

discovery  = DiscoveryV1(
  username='a27aee10-940d-4e8b-8eff-eb4c2ed94dc7',
  password='Nvb6rvXCpaYj',
  version='2017-11-07'
)


def discover():

    return "call"