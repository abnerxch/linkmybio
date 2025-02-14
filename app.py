from flask import Flask, render_template, jsonify, request
import yaml
import os
import datetime

developer = os.getenv("DEVELOPER", "User")
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)

class SocialMedia():
    def __init__(self, name, enable, link, description, picture, until):
        self.name = name
        self.enable = enable
        self.link = link
        self.description = description
        self.picture = picture
        self.until = until

listSocialLinks = []
with open("links.yaml", 'r') as stream:
    try:
        links = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
linkList = links.get("links")

for i in range(len(linkList)):
    picture = linkList[i].get(i+1).get("picture")
    name = linkList[i].get(i+1).get("name")
    enable = linkList[i].get(i+1).get("enable")
    link = linkList[i].get(i+1).get("link")
    description = linkList[i].get(i+1).get("description")
    until = linkList[i].get(i+1).get("until")

    social_media = SocialMedia(name, enable, link, description, picture, until)
    listSocialLinks.append(social_media)

@app.route('/')
def index():
    dateToday = datetime.datetime.now()

    dateNow = str(dateToday)
    return render_template("index.html", listSocialLinks=listSocialLinks, links=links, dateNow = dateNow)

if __name__ == '__main__':
  app.run(debug=True)