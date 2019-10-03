from flask import Flask, render_template, jsonify
import yaml, optparse
import os

developer = os.getenv("DEVELOPER", "User")
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)

info = yaml.load(open('links.yaml', 'r'))


links = []
for i in range(len(info['links'])):
    x = info['links'][i].get(i+1).get('link')
    links.append(x)

print(links[0])


@app.route('/')
def index():
    return render_template("index.html", name=info['name'], image=info['picture'], description=info['shortbio'], link=links)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)