#/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import json
from twitter import Twitter

def server():
    app = Flask(__name__)

    @app.route("/post", methods=["POST"])
    def post_twitt():
        text = request.json # receiver json = {"text": "Text Content Here"}

        if("text" not in text or len(text["text"]) < 1):
            return {"status":False}
        
        text = text["text"]
    
        twitter = Twitter()
        return twitter.post(text = text)

    @app.route("/search", methods=["GET"])
    def search_twitt():
        query = request.args.get("query", "")
            
        if(query == None or len(query) <= 1):
            return {"status":False}
            
        twitter = Twitter()
        return twitter.search(query=query)

    if __name__ == "__main__" : 
	    app.run()

server()