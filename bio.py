from flask import Flask, render_template, jsonify, request
import yaml, optparse
import os

developer = os.getenv("DEVELOPER", "User")
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)

class SocialMedia():
    def __init__(self, name, enable, link, description):
        self.name = name
        self.enable = enable
        self.link = link
        self.description = description

listSocialLinks = []
with open("links.yaml", 'r') as stream:
    try:
        links = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
linkList = links.get("links")

for i in range(len(linkList)):
    name = linkList[i].get(i+1).get("name")
    enable = linkList[i].get(i+1).get("enable")
    link = linkList[i].get(i+1).get("link")
    description = linkList[i].get(i+1).get("description")

    social_media = SocialMedia(name, enable, link, description)
    listSocialLinks.append(social_media)

@app.route('/')
def index():
    return render_template("index.html", social_media_list=listSocialLinks, links=links)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)