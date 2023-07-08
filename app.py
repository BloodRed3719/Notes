from flask import Flask, request, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate("firebase-key.json")  # Replace with your own Firebase service account key
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-firebase-project.firebaseio.com/'
})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def store():
    value = request.['value']

    # Save the value to Firebase Realtime Database
    ref = db.reference('/values')
    ref.push(value)

    return 'Value stored successfully!'

if __name__ == '__main__':
    app.run()
