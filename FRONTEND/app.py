from flask import Flask,render_template,url_for,redirect,request,jsonify,render_template_string
app = Flask(__name__)
import pandas as pd 
import tensorflow as tf
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, chi2
import numpy as np


import mysql.connector


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        address = request.form['Address']
        
        if password == confirmpassword:
            # Check if user already exists
            sql = 'SELECT * FROM users WHERE email = %s'
            val = (email,)
            mycur.execute(sql, val)
            data = mycur.fetchone()
            if data is not None:
                msg = 'User already registered!'
                return render_template('registration.html', msg=msg)
            else:
                # Insert new user without hashing password
                sql = 'INSERT INTO users (name, email, password, Address) VALUES (%s, %s, %s, %s)'
                val = (name, email, password, address)
                mycur.execute(sql, val)
                mydb.commit()
                
                msg = 'User registered successfully!'
                return render_template('registration.html', msg=msg)
        else:
            msg = 'Passwords do not match!'
            return render_template('registration.html', msg=msg)
    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    mydb = mysql.connector.connect(
    host='localhost',
    port=3306,          
    user='root',        
    passwd='',          
    database='botnetattack_new'  
    )

    mycur = mydb.cursor()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        sql = 'SELECT * FROM users WHERE email=%s'
        val = (email,)
        mycur.execute(sql, val)
        data = mycur.fetchone()

        if data:
            stored_password = data[3]  
            # Check if the password matches the stored password
            if password == stored_password:
                return redirect('/viewdata')
            else:
                msg = 'Password does not match!'
                return render_template('login.html', msg=msg)
        else:
            msg = 'User with this email does not exist. Please register.'
            return render_template('login.html', msg=msg)
    return render_template('login.html')

@app.route('/viewdata')
def viewdata():
    # Load the dataset
    df = pd.read_csv('UNSW_NB15.csv')
    df = df.head(1000)

    table_html = df.to_html(classes='table table-striped table-hover', index=False)
    return render_template('viewdata.html', table=table_html)

model_results = {
    'Hybrid': {
        'accuracy': 0.88,
    },
    'RandomForest': {
        'accuracy': 0.84,
    }
}

@app.route('/algo', methods=['GET', 'POST'])
def algo():
    model_name = request.form.get('model', 'Hybrid')

    result = model_results.get(model_name, model_results['Hybrid'])

    return render_template(
        'algo.html',
        accuracy=result['accuracy'],
        model_name=model_name
    )



# Load the saved model
rf_model = joblib.load('hybrid_model.pkl')

# Dictionary mapping encoded values to attack categories
attack_cat_mapping = {
    0: 'Analysis',
    1: 'Backdoor',
    2: 'DoS',
    3: 'Exploits',
    4: 'Fuzzers',
    5: 'Generic',
    6: 'Normal',
    7: 'Reconnaissance',
    8: 'Shellcode',
    9: 'Worms'
}


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        try:
            # Extract input data from the form
            input_data = [
                float(request.form['sbytes']),
                float(request.form['dbytes']),
                float(request.form['rate']),
                float(request.form['sload']),
                float(request.form['dload']),
                float(request.form['sinpkt']),
                float(request.form['sjit']),
                float(request.form['stcpb']),
                float(request.form['dtcpb']),
                float(request.form['response_body_len'])
            ]
            
            input_data = np.array([input_data])
            
            # Make prediction
            predicted_attack_idx = rf_model.predict(input_data)[0]
            predicted_attack_category = attack_cat_mapping[predicted_attack_idx]
            print(predicted_attack_category)
            return render_template('prediction.html', msg=f'Predicted Attack Category: {predicted_attack_category}')
        except Exception as e:
            return render_template('prediction.html', msg=f'Error: {str(e)}')
    return render_template('prediction.html')





 


if __name__ == '__main__':
    app.run(debug=True)