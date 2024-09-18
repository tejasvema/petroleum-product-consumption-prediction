from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
label_encoder=pickle.load(open('label_encoder.pkl','rb'))
# Month to numerical mapping
month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}

# Product names list and LabelEncoder
product_names = ['ATF', 'Bitumen', 'FO & LSHS', 'HSD', 'LDO', 'LPG', 'Lubricants & Greases',
                 'MS', 'Naphtha', 'Others', 'Petroleum coke', 'SKO']

label_encoder = LabelEncoder()
label_encoder.fit(product_names)

# Load the pre-trained RandomForest model (save your trained model beforehand)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    month = request.form['month']
    year = int(request.form['year'])
    product_name = request.form['product']

    # Convert month to numerical value
    month_num = month_map.get(month, None)
    if month_num is None:
        return "Invalid month name."

    # Encode the product name
    if product_name not in label_encoder.classes_:
        return f"Invalid product name: {product_name}."

    product_num = label_encoder.transform([product_name])[0]

    # Prepare the input data
    input_data = pd.DataFrame([[month_num, year, product_num]], columns=['Month', 'Year', 'PRODUCTS'])

    # Make the prediction
    predicted_quantity = model.predict(input_data)[0]

    # Return the predicted value to the user
    return render_template('result.html', predicted_quantity=predicted_quantity)

if __name__ == '__main__':
    app.run(debug=True)
