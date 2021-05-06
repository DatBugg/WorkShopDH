from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('oscar_pred.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    init_features = [float(x) for x in request.form.values()]
    final_features = [np.array(init_features)]

    prediction = model.predict(final_features)

    return render_template('index.html', prediction_text='Prediction: {}'.format(prediction))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)

    