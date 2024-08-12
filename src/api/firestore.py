from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, db
import uuid  # Import library uuid

app = Flask(__name__)

cred = credentials.Certificate("./boot-model-firebase-adminsdk-iqw0z-601a2fa03b.json")  # Firebase admin SDK
firebase_admin.initialize_app(cred, {"databaseURL": 'https://boot-model-default-rtdb.firebaseio.com'})

ref = db.reference('/')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Route to add a comment
@app.route('/add_comment', methods=['POST'])
def add_comment():
    comment = request.form.get('comment')

    unique_key = str(uuid.uuid4())  # Generate a unique key using uuid
    data = {
        'comment': comment,
        'key': unique_key,
    }
    ref.child('users').child(unique_key).set(data)  # Use ref.child() instead of db.collection()

    return jsonify({'status': 'Comment added successfully!'})  # Returns JSON

# Route to list all comments
@app.route('/list_comments', methods=['GET'])
def list_comments():
    comments = ref.child('users').get()  # Use ref.child() instead of db.collection()
    comments_list = []
    for comment in comments.items():
        comments_list.append(comment[1])

    return jsonify(comments_list)  # Returns JSON

if __name__ == '__main__':
    app.run(debug=True)
