from flask import Flask, render_template, request
import requests
from config import API_KEY, API_USERNAME, CATEGORY_ID, URL

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    params = {}

    if request.method == "POST":
        params["title"] = title = request.form.get("title")
        params["body"] =body = request.form.get("body")
        
        if not (title and body):
            params["error"] = "Both fields are required"
        else:
            headers = {
                "Api-Key": API_KEY,
                "Api-Username": API_USERNAME
            }

            payload = {
                "title": title,
                "raw": body,
                "category": CATEGORY_ID
            }

            try:
                resp = requests.post("{}/posts.json".format(URL),
                                    headers=headers,
                                    json=payload)
                params["success"] = True
            except:
                params["error"] = "Something wrong happened. Please try again later."

    return render_template("index.html", **params)

