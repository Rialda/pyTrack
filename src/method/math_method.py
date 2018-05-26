from __future__ import print_function
from collections import Counter
import csv

#['sentiment_score', row[0]
#  'sentiment_label', row[1]
# 'emotion_sadness', row[2]
# 'emotion_joy', row[3]
# 'emotion_fear', row[4]
#  'emotion_disgust', row[5]
#  'emotion_anger', row[6]
#  'influenza', row[7]
#  'sick', row[8]
#  'flu', row[9]
#  'headache', row[10]
#   'sore_throat', row[11]
#  'coughing', row[12]
#  'fever',  row[13]
# 'runny_nose'] row[14]

fileLikelihood="C:/Users/Rialda/PycharmProjects/pyTrack/src/method/likelihood.csv"
fileIliLabel="C:/Users/Rialda/PycharmProjects/pyTrack/src/method/ili_label.csv"

def math_method():
    f_ili_label = open(fileIliLabel, 'a')
    f_likelihood = open(fileLikelihood, 'a')
    with open('C:/Users/Rialda/PycharmProjects/pyTrack/src/method/formula_features.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            sentiment_score=row[0]
            sentiment_label=row[1]
            emotion_sadness=row[2]
            emotion_joy=row[3]
            emotion_fear=row[4]
            emotion_disgust=row[5]
            emotion_anger=row[6]

            flu=row[7]
            influenza=row[8]

            sore_throat=row[9]
            runny_nose=row[10]
            fatigue=row[11]
            sneezing=row[12]
            coughing=row[13]
            fever=row[14]
            headache=row[15]


            if float(sentiment_score) < 0:
                sentiment_value=3
            elif float(sentiment_score)==0:
                sentiment_value=2
            elif float(sentiment_score)>0:
                sentiment_value=1
            else:
                sentiment_value=0

            keywords=[influenza, flu]
            no_of_keywords=keywords.count('1')

            symptoms=[sore_throat,runny_nose,fatigue,sneezing,coughing,fever,headache]
            no_of_symptoms=symptoms.count('1')

            if emotion_disgust!='0' and emotion_joy!='0' and emotion_joy!='0' and emotion_anger!='0' and emotion_fear!='0' and emotion_sadness!='0':
                emotions=[emotion_anger,emotion_disgust,emotion_fear,emotion_joy,emotion_sadness]
                max_emo=max(emotions)
                if max_emo==emotion_sadness:
                    emotional_value=5
                elif max_emo==emotion_fear or max_emo==emotion_anger:
                    emotional_value=4
                elif max_emo==emotion_disgust:
                    emotional_value=2
                elif max_emo==emotion_joy:
                    emotional_value=1
            else:
                emotional_value=0
            feature_set_one=(no_of_symptoms+no_of_keywords+sentiment_value)/11
            feature_set_two=(emotional_value)/5
            likelihood=feature_set_one+feature_set_two

            if (((no_of_keywords+no_of_symptoms)>=1) and sentiment_value>=2 and  emotional_value>=2):
                ili_label="True"
            else:
                ili_label="False"
            f_ili_label.write(str(ili_label)+'\n')
            f_likelihood.write(str(likelihood)+'\n')
            print(no_of_symptoms+no_of_keywords, sentiment_value, emotional_value)