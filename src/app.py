# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
api = Api(app)

# Function for feature engineering 
def preprocess(df):
    # Log of loan amount
    df['LoanAmountLog'] = np.log(df['LoanAmount'].astype('float64')) 
    # Total income and log of total income
    df['Total_Income'] = df['ApplicantIncome'] + df['CoapplicantIncome']
    df['Total_Income_log'] = np.log(df['Total_Income'].astype('float64'))

    # Drop the original features
    cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']
    df = df.drop(columns=cols)

    return df


model = pickle.load( open('LogRegModel.pickle', 'rb' ) )       



class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        
        # getting predictions from the model
        res = model.predict_proba(df)
    
        return(f'The probability of loan refusal for this individual is {res[0][0]*100:.1f}%.')
        return(f'The probability of loan approval for this individual is {res[0][1]*100:.1f}%.')
        # return res.tolist() 
    
# assign endpoint
api.add_resource(Scoring, '/scoring')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)
