# import os
from flask import Flask, url_for
from flask import json

# data_folder_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

app = Flask(__name__)
# app.config['DATA_FOLDER'] = data_folder_root

@app.route('/', methods = ['GET'])
def api_root():
    return 'Welcome'

@app.route('/tagreads', methods = ['GET'])
def api_tagreads():
    # filename = os.path.join(app.config['DATA_FOLDER'], 'articles.txt')
    # with open(filename, 'r') as f:
    #     data = f.read()
    #     return 'List of ' + data
    return 'Listing all tagged info'

@app.route('/tagreads/<tagid>', methods = ['GET'])
def api_tagread(tagid):
    return 'You are reading ' + tagid

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
