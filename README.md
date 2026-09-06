# 🧠 Sentiment Analysis using Naive Bayes

A Machine Learning web application that performs **sentiment analysis on text reviews** and classifies them as **Positive** or **Negative**.

The project uses **Natural Language Processing (NLP)** techniques and a **Multinomial Naive Bayes** classifier. The trained model is deployed using **Flask**.

## 🚀 Project Overview

Sentiment Analysis is an NLP task used to determine the emotional tone of a piece of text.

This project takes a user's review as input and predicts whether the sentiment is:

* 😊 **Positive**
* 😞 **Negative**

### Example

```text
Input:
"This product is amazing and works perfectly!"

Output:
Positive
```

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**
* **NLTK**
* **Flask**
* **HTML / CSS**
* **TF-IDF Vectorization**
* **Multinomial Naive Bayes**
* **Joblib**

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Text Preprocessing
   ↓
Train / Test Split
   ↓
TF-IDF Vectorization
   ↓
Multinomial Naive Bayes
   ↓
Model Evaluation
   ↓
Save Model
   ↓
Flask Web Application
   ↓
User Input
   ↓
Sentiment Prediction
```

## 📂 Project Structure

```text
sentiment/
│
├── app.py
├── preprocessor.py
├── sentiment.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
```

## 🧹 Text Preprocessing

Before sending text to the machine learning model, the input is processed to improve prediction quality.

Typical preprocessing steps include:

* Converting text to lowercase
* Removing unnecessary characters
* Removing stopwords
* Cleaning whitespace
* Preparing text for vectorization

## 🔢 TF-IDF Vectorization

The cleaned text is converted into numerical features using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

TF-IDF helps the model understand which words are important within the review.

## 🤖 Machine Learning Model

The project uses **Multinomial Naive Bayes**, a popular classification algorithm for text-based NLP problems.

The model learns patterns from labeled reviews and predicts the sentiment of new text.

## 🌐 Flask Deployment

The trained model and TF-IDF vectorizer are saved using `joblib`.

```text
sentiment.pkl
vectorizer.pkl
```

The Flask application loads these files and uses them to make predictions from user input.

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/gogulvkn/sentiment.git
```

### 2. Navigate to the project

```bash
cd sentiment
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Flask application

```bash
python app.py
```

### 7. Open in your browser

```text
http://127.0.0.1:5000/
```

## 💡 Example Predictions

| Review                       | Prediction  |
| ---------------------------- | ----------- |
| `I really love this product` | 😊 Positive |
| `The product is excellent`   | 😊 Positive |
| `Very bad experience`        | 😞 Negative |
| `I don't like this product`  | 😞 Negative |

## 📌 Future Improvements

* Add **Positive / Negative confidence score**
* Add **Neutral sentiment**
* Improve NLP preprocessing
* Try different ML algorithms
* Add confusion matrix and classification report
* Improve frontend design
* Deploy the application online
* Add REST API support

## 🎯 Learning Outcomes

Through this project, I learned how to:

* Work with text data
* Perform NLP preprocessing
* Convert text into numerical features
* Train a Naive Bayes classifier
* Evaluate a machine learning model
* Save and load trained ML models
* Build a Flask web application
* Deploy a machine learning project

## 👨‍💻 Author

**kamatchinthan v**

GitHub:
https://github.com/gogulvkn

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
