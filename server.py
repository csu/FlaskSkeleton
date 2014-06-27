#!/usr/bin/env python
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# client = MongoClient('mongodb://localhost:27017/')
# db = client.DATABASE_NAME
# collection = db.COLLECTION_NAME

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', header='Flask Skeleton', title='Flask Skeleton', body='''
        <p>Some content can go here!</p>
        ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)