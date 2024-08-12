import pyrebase
from flask import Flask, request, jsonify

config = {
    'apiKey': "AIzaSyCuZi3jf1RMbXo4OGco4aD3rMGrh5dtLk8",
    'authDomain': "boot-model.firebaseapp.com",
    'projectId': "boot-model",
    'storageBucket': "boot-model.appspot.com",
    'messagingSenderId': "95509509849",
    'appId': "1:95509509849:web:96609e7626f788368870c8"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)

@app.route('/create', methods=['POST'])

def create():
    username = request.form.get('username')
    userage = request.form.get('userage')
    userid = request.form.get('userid')

    unique_Key = db.generate_key()
    data = {
        'username': username,
        'userage': userage,
        'userid': userid,
        'key': unique_Key,
    }
    db.child('users').child(unique_Key).set(data)

    return jsonify({'status': str('Data add successfully!')})

@app.route('/read', methods=['POST'])
def read():
    username = request.form.get('username')

    users = db.child('users').get()
    for user in users.each():
        if user.val()['username'] == username:
            x = db.child('users').child(user.key()).get().val()
            return jsonify(x)
        return jsonify({'status': str('There is no such name in the database!')})
    
if __name__ == '__main__':
    app.run(debug=True)

