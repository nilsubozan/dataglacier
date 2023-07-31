from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

#Load the trained model and encoders
model = joblib.load('LR_dataglacier_model.pkl')
encoders = {'Gender': joblib.load('gender_encoder.pkl'), 'Profession': joblib.load('profession_encoder.pkl')}

@app.route('/', methods=['GET'])
def index():
    return render_template('template.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = request.form.to_dict()
        new_data = pd.DataFrame([data])

        #Encode categorical columns
        for column in ['Gender', 'Profession']:
            encoder = encoders[column]
            new_data[column+'_encoded'] = encoder.transform(new_data[column])

        #Drop original columns
        new_data.drop(['Gender', 'Profession'], axis=1, inplace=True)

        #Make predictions
        predictions = model.predict(new_data)

        return jsonify(predictions.tolist())

    return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True)