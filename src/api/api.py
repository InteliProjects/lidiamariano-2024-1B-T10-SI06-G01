import slack
import slack_sdk
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from nltk.corpus import stopwords as sw
from nltk.tokenize import WhitespaceTokenizer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import re
import pickle
import pandas as pd
import firebase_admin
import fasttext
from firebase_admin import credentials, storage
from flask_cors import CORS
import logging
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import fbeta_score
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_REGION = ''
S3_BUCKET = ''


s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)




logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
CORS(app)

# Starting firebase
cred = credentials.Certificate(
    "./boot-model-firebase-adminsdk-iqw0z-601a2fa03b.json")  # Firebase admin SDK
firebase_admin.initialize_app(
    cred, {"storageBucket": 'boot-model.appspot.com'})


modelo_fasttext = fasttext.load_model('./model/fasttext_model_hs.bin')

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])


def vectorize(text, model):
    return model.get_sentence_vector(text)


def preprocess(text):
    """
    Endpoint for receiving a CSV file via POST request and uploading it to Firebase Storage.

    The file is received as part of the request files. If no file is received, or if the file
    is not a CSV file, an error message is returned as JSON.

    If the file is successfully uploaded to Firebase Storage, a download URL for the file is
    generated and returned as JSON.

    If an error occurs during this process, it is caught and returned as JSON.

    Returns:
        JSON response with either the download URL for the uploaded file, or an error message.
    """
    return text.lower()

# trigger part

def calculate_tweet_length(tweet):
    """
    Calculates the length of a tweet.

    Args:
        tweet (str): The input tweet.

    Returns:
        int: The length of the tweet.
    """
    return len(tweet)

def predict_proba(text_vector):
    """
    Predicts the probability of the text belonging to a certain class.

    Args:
        text_vector (np.array): The vectorized form of the text.

    Returns:
        list: The probability scores.
    """
    proba_scores = modelo_svm.predict_proba(text_vector)
    logging.debug(f'Probability Scores: {proba_scores}')
    return proba_scores[0]

def calculate_viral_score(likes, comments, length, decision_score):
    """
    Calculates the viral score of a tweet.

    Args:
        likes (int): Number of likes.
        comments (int): Number of comments.
        length (int): Length of the tweet.
        decision_score (float): Decision function score.

    Returns:
        float: The viral score.
    """
    return 0.4 * likes + 0.3 * comments + 0.1 * length + 0.2 * decision_score

def send_alert_to_slack(prediction, probability, threshold, viral_score, tweet):
    """
    Sends an alert to Slack with the prediction and probability.

    Args:
        prediction (int): The sentiment prediction.
        probability (float): The predicted probability.
        threshold (float): The threshold value.
        viral_score (float): The calculated viral score.
        tweet (str): The text of the tweet.

    Returns:
        None
    """
    channel = '#sentiment_tracker_inteli'
    prediction_text = 'Negative' if prediction == 1 else 'Positive'
    prediction_emoji = '🔴' if prediction == 1 else '🔵'
    probability_percent = round(probability * 100, 2)
    
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"📢 Improvement Comment Alert {prediction_emoji}"
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*Prediction:* {prediction_text} {prediction_emoji}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*Probability:* {probability_percent}% 📊"
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🗨️ *Tweet:* {tweet}"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "🚨 *Alert Type:* Event"
                },
                {
                    "type": "mrkdwn",
                    "text": "📈 *Trend:*"
                },
                {
                    "type": "mrkdwn",
                    "text": "<Service Quality> <Price> <Convenience>"
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "🔗 *Link to Sample Comment:*"
                },
                {
                    "type": "mrkdwn",
                    "text": "<https://twitter.com/?lang=pt-br>"
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "🌐 *Platform:* Twitter"
                },
                {
                    "type": "mrkdwn",
                    "text": "🚗 *Asset Name:* Uber"
                },
                {
                    "type": "mrkdwn",
                    "text": "🖼️ *Post Type:* Media Post"
                },
                {
                    "type": "mrkdwn",
                    "text": "🔗 *Post Linked:* +99"
                }
            ]
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "🔍 View on Twitter"
                    },
                    "url": "https://twitter.com/?lang=pt-br"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "✅ Mark as Resolved"
                    },
                    "style": "primary",
                    "value": "resolved"
                }
            ]
        }
    ]

    client.chat_postMessage(channel=channel, blocks=blocks)




def calculate_youden_index(conf_matrix):
    """
    Calculate Youden's Index from the confusion matrix.
    """
    # Assuming binary classification for simplicity
    TP = conf_matrix[1, 1]
    FN = conf_matrix[1, 0]
    FP = conf_matrix[0, 1]
    TN = conf_matrix[0, 0]
    sensitivity = TP / (TP + FN)
    specificity = TN / (TN + FP)
    youden_index = sensitivity + specificity - 1
    return youden_index


@app.route("/")
def hello_world():
    return "<p>Boot!!</p>"


with open('./model/svm_model.pkl', 'rb') as file:
    modelo_svm = pickle.load(file)


@app.route("/upload_s3", methods=["POST"])
def upload_csv_s3():
    """
    Endpoint for receiving a CSV file via POST request and uploading it to Amazon S3.

    The file is received as part of the request files. If no file is received, or if the file
    is not a CSV file, an error message is returned as JSON.

    If the file is successfully uploaded to Amazon S3, a download URL for the file is
    generated and returned as JSON.

    If an error occurs during this process, it is caught and returned as JSON.

    Returns:
        JSON response with either the download URL for the uploaded file, or an error message.
    """
    try:
        if "file" not in request.files:  # Verifying if file was uploaded
            return jsonify({"error": "No files sent"}), 400

        file = request.files["file"]

        if not file.filename.endswith(".csv"):  # Verifying if file is .CSV
            return jsonify({"error": "The file must be a CSV"}), 400

        # Upload file to S3
        s3_client.upload_fileobj(
            file,
            S3_BUCKET,
            "uploads/" + file.filename
        )

        # Generate download URL
        download_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': S3_BUCKET, 'Key': "uploads/" + file.filename},
            ExpiresIn=3600
        )

        return jsonify({"success": True, "download_url": download_url}), 200
    except (NoCredentialsError, PartialCredentialsError) as e:
        return jsonify({"error": "AWS credentials not available"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/upload", methods=["POST"])
def upload_csv():
    """
    Endpoint for receiving a CSV file via POST request and uploading it to Firebase Storage.

    The file is received as part of the request files. If no file is received, or if the file
    is not a CSV file, an error message is returned as JSON.

    If the file is successfully uploaded to Firebase Storage, a download URL for the file is
    generated and returned as JSON.

    If an error occurs during this process, it is caught and returned as JSON.

    Returns:
        JSON response with either the download URL for the uploaded file, or an error message.
    """
    try:
        if "file" not in request.files:  # Verifying if file was uploaded
            return jsonify({"error": "No files sent"}), 400

        file = request.files["file"]

        if not file.filename.endswith(".csv"):  # Verifying if file is .CSV
            return jsonify({"error": "The file must be a CSV"}), 400

        # Upload file to Firebase Storage
        bucket = storage.bucket()
        blob = bucket.blob("uploads/" + file.filename)
        blob.upload_from_file(file)

        # Return file URL on Firebase Storage
        download_url = blob.generate_signed_url(
            expiration=3600)
        return jsonify({"success": True, "download_url": download_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/predict_csv', methods=['POST'])
def predict_csv():
    """
    Endpoint for receiving a CSV file, processing its content, and making predictions.

    The CSV file should have a column named 'text' containing the text data to be analyzed.
    """
    try:
        if "file" not in request.files:  # Verifying if file was send
            return jsonify({"error": "No files sent"}), 400

        file = request.files["file"]

        if not file.filename.endswith(".csv"):  # Verifying if file is a CSV
            return jsonify({"error": "The file must be a CSV"}), 400

        # Read CSV into a Dataframe
        df = pd.read_csv(file, sep=';')
        if 'comment' not in df.columns:
            return jsonify({"error": "CSV must contain a 'comment' column"}), 400

        # Preprocess and vectorize each text in CSV
        df['preprocessed_text'] = df['comment'].apply(preprocess)
        df['vector'] = df['preprocessed_text'].apply(
            lambda x: vectorize(x, modelo_fasttext).reshape(1, -1)
        )

        # Make predictions for each vector
        df['prediction'] = df['vector'].apply(
            lambda x: modelo_svm.predict(x)[0])

        # Returns the predictions
        predictions = df[['comment', 'prediction']].to_dict(orient='records')
        return jsonify({'predictions': predictions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/preprocessing', methods=['POST'])
def preprocess_text():
    """
    Preprocesses a given text by removing stopwords, URLs, punctuation, and numbers.

    This function takes a text input from a POST request, tokenizes the text using a WhitespaceTokenizer,
    and removes stopwords, URLs, punctuation, and numbers from the text. The cleaned text is returned.

    Returns:
    str: The processed text.
    """
    nltk.download('stopwords')

    # Get the text from the POST request
    data = request.get_json()
    text = data.get('text', '')

    # Define stopwords and tokenizer
    stopwords = set(sw.words('english'))
    token_space = WhitespaceTokenizer()

    # Tokenize the text
    word_text = token_space.tokenize(text)

    # Process the text
    new_comment = [w.lower() for w in word_text if w.lower() not in stopwords]
    new_comment = [re.sub(r'http\S+|www.\S+', '', word)
                   for word in new_comment]
    new_comment = [re.sub(r'[^\w\s]', '', word)
                   for word in new_comment]  # remove punctuation
    new_comment = [re.sub(r'\d+', '', word)
                   for word in new_comment]  # remove numbers

    processed_text = ' '.join(new_comment)

    return jsonify({'processed_text': processed_text})


@app.route('/vectorize', methods=['POST'])
def vectorize_text():
    """
    Vectorizes the pre-processed text using the vectorize function.

    This function takes a pre-processed text input from a POST request and returns its vector representation.

    Returns:
    list: The vectorized form of the text.
    """
    # Get the pre-processed text from the POST request
    data = request.get_json()
    processed_text = data.get('processed_text', '')

    # Vectorize the text
    vector = vectorize(processed_text, modelo_fasttext)

    return jsonify({'vector': vector})


@app.route('/predict', methods=['POST'])
def predict():
    """
    Receives a text and returns the sentiment prediction using SVM
    """
    try:
        # Receive the text of POST request
        data = request.get_json()
        texto = data.get('text', '')

        # Preprocessing and vectorizer the text
        texto_preprocessado = preprocess(texto)
        vetor_texto = vectorize(texto_preprocessado, modelo_fasttext).reshape(
            1, -1)

        # Make prediction with the SVM Classifier
        predicao = modelo_svm.predict(vetor_texto)

        # Return the predition as JSON
        return jsonify({'prediction': int(predicao[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/pipeline', methods=['POST'])
def predict_and_send():
    """
    Predict sentiment and send an alert to Slack if the viral score exceeds the threshold.

    This endpoint receives a JSON payload with a 'text' field, processes the text,
    makes a sentiment prediction, calculates the viral score based on likes and comments,
    and sends an alert to Slack if the viral score exceeds a predefined threshold.

    Returns:
        JSON: A response containing the prediction, viral score, decision score, and threshold.
    """
    try:
        # Receive text from POST request
        data = request.get_json()
        texto = data.get('text', '')

        # Preprocess and vectorize text
        texto_preprocessado = preprocess(texto)
        vetor_texto = vectorize(texto_preprocessado, modelo_fasttext).reshape(1, -1)

        # Simulate likes and comments
        likes = 100  # Simulated value for likes
        comments = 20  # Simulated value for comments

        # Make prediction with the classifier
        predicao = modelo_svm.predict(vetor_texto)[0]
        probabilidade = modelo_svm.predict_proba(vetor_texto)[0]
        decision_score = max(probabilidade)  # Use the max probability as decision score

        # Calculate tweet length and viral score
        tweet_length = calculate_tweet_length(texto)
        viral_score = calculate_viral_score(likes, comments, tweet_length, decision_score)

        # Define the threshold value
        threshold = 60  # Example threshold value (between 60-70 seems to be a good range for a viral score)

        # Check if viral score exceeds threshold and send alert to Slack if it does
        if viral_score >= threshold:
            send_alert_to_slack(predicao, decision_score, threshold, viral_score, texto)

        # Return prediction, viral score, decision score, and threshold as JSON
        return jsonify({'prediction': int(predicao), 'viral_score': viral_score, 'decision_score': float(decision_score), 'threshold': threshold})
    except Exception as e:
        # Return error message as JSON if an exception occurs
        return jsonify({'error': str(e)}), 400



@app.route('/results', methods=['GET'])
def get_results():
    """
    Retrieves and displays stored results.
    """
    try:
        y_test = modelo_fasttext['y_test']
        y_pred = modelo_fasttext['y_pred']
        labels = modelo_fasttext['labels']
        # Calculate metrics
        accuracy_test = accuracy_score(y_test, y_pred)
        precision_test = precision_score(y_test, y_pred, average='weighted')
        recall_test = recall_score(y_test, y_pred, average='weighted')
        f1_score_test = fbeta_score(y_test, y_pred, beta=2, average='weighted')
        #cohen_kappa_test = cohen_kappa_score(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)
        youden_index_test = calculate_youden_index(conf_matrix)
        # Return results as JSON
        return jsonify({
            'accuracy': accuracy_test,
            'precision': precision_test,
            'recall': recall_test,
            'f1_score': f1_score_test,
            # 'cohen_kappa': cohen_kappa_test,
            'confusion_matrix': conf_matrix.tolist(),
            'youden_index': youden_index_test
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
