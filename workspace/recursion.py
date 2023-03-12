#Purpose: This is a decision-tree based algorithm that handles predetermined
#         categorical constants within ordinal data (categories have inherent order)

#Citation: javatpoint.com/machine-learning-decision-tree-classification-algorithm
#          Machine Learning Tutorial Python - 9 Decision Tree by codebasics on YouTube

import matplotlib.pyplot as mtp
import pandas as pd
import numpy as nm

def decision_tree():
    
    # Import survey data
    data = pd.read_csv('survey_data.csv')
    inputs = data.drop('Boolean', axis='columns')
    target = data['Boolean']


    # Transforming quantatative data into numeric data used for machine training
    from sklearn.preprocessing import LabelEncoder
    enc_Subject = LabelEncoder()
    enc_Type = LabelEncoder()
    enc_Estimated_Time = LabelEncoder()
    enc_Occurence = LabelEncoder()

    inputs['Subject_enc'] = enc_Subject.fit_transform(inputs['Subject'])
    inputs['Type_enc'] = enc_Type.fit_transform(inputs['Type'])
    inputs['Estimated_Time_enc'] = enc_Estimated_Time.fit_transform(inputs['Estimated_Time'])
    inputs['Occurence_enc'] = enc_Occurence.fit_transform(inputs['Occurence'])

    inputs_enc = inputs.drop(['Subject', 'Type', 'Estimated_Time', 'Occurence'], axis='columns')


    print(inputs_enc)

    # Prediction model
    from sklearn import tree
    model = tree.DecisionTreeClassifier(criterion='entropy', random_state=0)
    model.fit(inputs_enc, target)
    model.score(inputs_enc, target)

    #Grab last row from database
    sub = inputs_enc.iloc[-1,0]
    typ = inputs_enc.iloc[-1,1]
    times = inputs_enc.iloc[-1,2]
    occur =  inputs_enc.iloc[-1,3]

    pred = int(model.predict([[sub,typ,times,occur]]))

    return pred