from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import re

def clean_text(text):
    output = text.lower()
    output = re.sub(r'[^A-Za-z0-9 ]+','',output)
    return output

model = joblib.load('tree_model.pkl')
vectorizer = joblib.load('tree_vectorizer.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        cleaned_title = clean_text(title)
        cleaned_text = clean_text(text)
        combined_text = cleaned_title + ' ' + cleaned_text
        vec = vectorizer.transform([combined_text])
        prediction = model.predict(vec)[0]
        if prediction == 0:
            return jsonify({'prediction': 'FAKE NEWS'})
        else:
            return jsonify({'prediction': 'REAL NEWS'})
    return render_template('index.html')     
        
if __name__ == '__main__':
    app.run(debug=True)