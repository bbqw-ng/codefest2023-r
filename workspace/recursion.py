#Purpose: This is a decision-tree based algorithm that handles predetermined
#         categorical constants within ordinal data (categories have inherent order)

#Citation: javatpoint.com/machine-learning-decision-tree-classification-algorithm
#          Machine Learning Tutorial Python - 9 Decision Tree by codebasics on YouTube

import matplotlib.pyplot as mtp
import pandas as pd
import numpy as nm

if __name__ == "__main__":
    
    # Import survey data
    data = pd.read_csv('survey_data.csv')
    inputs = data.drop('Boolean', axis='columns')
    target = data['Boolean']


    # Transforming quantatative data into numeric data used for machine training
    from sklearn.preprocessing import LabelEncoder
    enc_Subject = LabelEncoder()
    enc_Type = LabelEncoder()
    enc_Purpose = LabelEncoder()
    enc_Occurence = LabelEncoder()

    #debug
    inputs.head()

    inputs['Subject_enc'] = enc_Subject.fit_transform(inputs['Subject'])
    inputs['Type_enc'] = enc_Type.fit_transform(inputs['Type'])
    inputs['Purpose_enc'] = enc_Subject.fit_transform(inputs['Purpose'])
    inputs['Occurence_enc'] = enc_Subject.fit_transform(inputs['Occurence'])

    inputs_enc = inputs.drop(['Subject', 'Type', 'Purpose', 'Occurence'], axis='columns')

    #debug
    inputs_enc

    from sklearn import tree
    model = tree.DecisionTreeClassifier()
    print(model)
    model.fit(inputs_enc, target)
    model.score(inputs_enc, target)