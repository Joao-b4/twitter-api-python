#/usr/bin/python3
# -*- coding: utf-8 -*-
import oauth2
import json 
import urllib.parse

class Twitter:

    consumer_key = "CONSUMER KEY HERE"
    consumer_secret = "CONSUMER SECRET HERE"

    access_token = "ACCESS TOKEN HERE"
    access_token_secret = " ACCESS TOKEN SECRET HERE"

    consumer = oauth2.Consumer(consumer_key,consumer_secret)
    token = oauth2.Token(access_token,access_token_secret)
    client = oauth2.Client(consumer,token)

    def post(self, text = ""):
        text_codefy = urllib.parse.quote(text, safe="")
        request = self.__class__.client.request("https://api.twitter.com/1.1/statuses/update.json?status="+str(text_codefy),method='POST')
        request_decode = request[1].decode()
        request_object = json.loads(request_decode)
        
        if "errors" in request_object:
            request_object["status"] = False
        else:
            request_object["status"] = True

        return request_object
        

    def search(self, query = ""):
        query_codefy = urllib.parse.quote(query, safe="")
        request = self.__class__.client.request("https://api.twitter.com/1.1/search/tweets.json?q="+str(query_codefy))
        request_decode = request[1].decode()
        request_object = json.loads(request_decode)

        twittes = request_object["statuses"]
        response_array = []

        for twitt in twittes:
            user = twitt["user"]["screen_name"]
            text = twitt["text"]
            response_array.append({"user": user, "text": text})

        return {"status": True, "response": response_array}
