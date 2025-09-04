#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "<h2>Linear Regression Model API</h2><p>Use /predict with POST method to make predictions.</p>"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Example: {"features": [5, 10, 20]}
        features = np.array(data["features"]).reshape(1, -1)

        # Predict using model
        prediction = model.predict(features)

        return jsonify({
            "input": data["features"],
            "prediction": prediction.tolist()
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




