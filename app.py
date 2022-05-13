import os
from flask import Flask, request
from calender_scraper import get_events

# coisas do site
app = Flask(__name__)

@app.route("/")
def hello_world():
	arquivo = open("templates/home.html")
	return arquivo.read()

def display_events():
	events = get_events("maio", "pt")
	return f"""
	{events}
	"""
