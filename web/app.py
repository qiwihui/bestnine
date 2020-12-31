# coding: utf-8
import os
from flask import Flask, session
from flask_restful import Resource, Api, request
from requests_oauthlib import OAuth2Session
from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
api = Api(app)

API_CLIENT_ID = "1741082089386595"
API_CLIENT_SECRET = "edbfc4738c13816753742787ac7a3e51"
authorization_base_url = "https://api.instagram.com/oauth/authorize"
token_url = "https://api.instagram.com/oauth/access_token"


class AccessToken(Resource):
    def post(self):
        code = request.json["code"]
        print(code)
        session["oauth_state"] = 1
        instagram = OAuth2Session(
            client_id=API_CLIENT_ID,
            state=session["oauth_state"],
            redirect_uri="https://bestnine.qiwihui.com/",
        )
        token = instagram.fetch_token(
            token_url,
            client_secret=API_CLIENT_SECRET,
            code=code,
            include_client_id=True,
        )
        session["oauth_token"] = token
        print(token)

        return {
            "status": "ok",
            "data": {
                "token": token,
            },
        }, 201


api.add_resource(AccessToken, "/api/access_token")


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True)
