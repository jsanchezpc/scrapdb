from flask import Flask, render_template, request, redirect, session
from flaskwebgui import FlaskUI
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
app.secret_key = "seed-x-secret"


@app.route("/")
def home():
    return render_template('index.html', images=[])


@app.route("/get_from_url", methods=['POST', 'GET'])
def get_from_url():
    linput = request.form["linput"]
    print(linput)
    linput = requests.get(linput)
    soup = BeautifulSoup(linput.text, 'html.parser')
    images = soup.find_all('img')
    images = images[1:]
    print(images)
    return render_template('index.html', images=images)


@app.route("/get_from_query", methods=['POST', 'GET'])
def get_from_query():
    search = request.form["qinput"]
    search = search.replace(' ', "+")
    url = f'https://www.google.com/search?q={search}&tbm=isch'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    images = images[1:]
    return render_template('index.html', images=images)


@app.route("/collection")
def collection():
    return render_template('collection.html')


@app.route('/error')
def error():
    return render_template('error.html')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    #app.run(debug=True)
      FlaskUI(app=app, server="flask", browser_path="C:\Program Files\Google\Chrome\Application\chrome.exe").run()