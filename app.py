from flask import Flask, request, render_template
import joblib
import re

app = Flask(__name__)

from preprocessor import clean_text 


# Load models safely
try:
    vectorizer = joblib.load('vectorizer.pkl')
    model = joblib.load('sentiment.pkl')
    print("Model and Vectorizer loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")
    vectorizer, model = None, None

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_result = None
    error_message = None
    user_text = ""

    if request.method == 'POST':
        user_text = request.form.get('text', '')
        
        # Validation check
        if not clean_text(user_text):
            error_message = "Invalid input. Text contains no readable words."
        else:
            if model and vectorizer:
                X_vec = vectorizer.transform([user_text])
                raw_pred = model.predict(X_vec)[0]
                
                # Convert prediction format nicely
                prediction_result = str(raw_pred).strip("['']")

                if raw_pred == 1:
                    prediction_result = "Positive"
                else:
                    prediction_result = "Negative"

                
            else:
                error_message = "Model files are missing on the server."

    return render_template('index.html', 
                           prediction=prediction_result, 
                           error=error_message, 
                           input_text=user_text)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
