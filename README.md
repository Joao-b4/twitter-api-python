# twitter-api-python
api to post and search tweets, developed in python, using flask.

### Requirements
- pip3 install flask
- pip3 install oauth2
- pip3 install json

### Changes
 - modify tokens and consumer_key in twitter.py
 

### Use
- python main.py

### Routes
- POST:  http://127.0.0.1/post?text=HereTextPost
    - Body:  {"text": "status content here"}
- GET:  http://127.0.0.1/search?query=HereTextQuery

