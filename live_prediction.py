import pandas as pd
import numpy as np
import pickle

model = pickle.load(open("random_forest_model.pkl", "rb"))
# df = pd.DataFrame(columns=["Day-Part", "Start Time", "End Time"])
gender = input("Enter Gender of the Participant - Male/Female").lower()
Polyuria = input("Does the participant have Polyuria? - Yes/ No").lower()
Polydipsia = input("Does the participant have Polydipsia? - Yes/ No").lower()
sudden_weight_loss = input("Has the participant experienced sudden weight loss? - Yes/ No").lower()
weakness = input("Does the participant feel any weakness? - Yes/ No").lower()
Polyphagia = input("Does the participant have Polyphagia? - Yes/ No").lower()
Genital_thrush = input("Does the participant have Genital thrush? - Yes/ No").lower()
visual_blurring = input("Does the participant have visual blurring? - Yes/ No").lower()
Itching = input("Does the participant have Itching? - Yes/ No").lower()
Irritability = input("Does the participant have Irritability? - Yes/ No").lower()
delayed_healing = input("Does the participant have delayed healing? - Yes/ No").lower()
partial_paresis = input("Does the participant have partial paresis? - Yes/ No").lower()
muscle_stiffness = input("Does the participant have muscle stiffness? - Yes/ No").lower()
Alopecia = input("Does the participant have Alopecia? - Yes/ No").lower()
Obesity = input("Does the participant have Obesity? - Yes/ No").lower()
age = int(input("Enter Age of Participant as a number"))

df1 = pd.DataFrame(data=[[gender,Polyuria,Polydipsia,sudden_weight_loss,weakness,Polyphagia,Genital_thrush,visual_blurring,Itching,Irritability,delayed_healing,
                          partial_paresis,muscle_stiffness,Alopecia,Obesity,age]],columns=['Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss', 'weakness', 'Polyphagia',
                                              'Genital thrush', 'visual blurring', 'Itching', 'Irritability', 'delayed healing', 'partial paresis',
                                              'muscle stiffness', 'Alopecia', 'Obesity','Age'])

print(df1)

df1 = df1.replace({'no': 0, 'yes': 1, "n": 0, "y": 1})
df1 = df1.replace({'female': 0, 'male': 1, 'f': 0, 'm': 1})
type1list = [sudden_weight_loss,Polyuria,visual_blurring,weakness,Alopecia,Irritability]
type2list = [sudden_weight_loss,Polyuria,visual_blurring,weakness,Polydipsia,Polyphagia,Itching,delayed_healing,muscle_stiffness]
type1count = 0
for i in type1list:
    if (i == 'yes') or (i == 'y'):
        type1count = type1count +1
type2count = 0
for i in type2list:
    if (i == 'yes') or (i == 'y'):
        type2count = type2count +1
        
    
print(df1)
prediction = model.predict(df1)[0]
if prediction == 1:
    pred = "positive"
    if type2count > 4:
        type = "Type II"
    else:
        type = "Type I"
elif prediction == 0:
    pred = "negative"
    type = None
print("prediction:",pred)
if type is not None:
    print("type:",type)

