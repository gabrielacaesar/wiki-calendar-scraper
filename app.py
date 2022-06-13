import os
import flask, json
from flask import Flask, request, jsonify, after_this_request
from scraper_calendar import get_events
from github import Github

# coisas do site
app = Flask(__name__)

@app.route("/")
def hello_world():
	arquivo = open("templates/home.html")
	return arquivo.read()

@app.route("/events", methods=['GET'])
def get_content():
    @after_this_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
        
    month = str(request.args['month'])
    lang = str(request.args['lang'])
    print(month)
    print(lang)

    try:
        output = get_events(month, lang)

    except ValueError as e:
        return {"error":1}

    return output

@app.route("/en-june")
def display_en():
	events = get_events("June", "en")
	html_events = events.to_html()
	return f""""
	{html_events}
	"""

@app.route("/pt-junho")
def display_pt():
	events = get_events("junho", "pt")
	html_events = events.to_html()
	return f""""
	{html_events}
	"""

@app.route("/de-juni")
def display_de():
	events = get_events("Juni", "de")
	html_events = events.to_html()
	return f""""
	{html_events}
	"""

@app.route("/es-junio")
def display_es():
	events = get_events("junio", "es")
	html_events = events.to_html()
	return f""""
	{html_events}
	"""

@app.route("/calendar")
def display_events():
	events = get_events("maio", "pt")
	html_events = events.to_html()
	return f""""
	{html_events}
	"""

### tentativa com aula do lucas
TOKEN_GITHUB = os.environ["API_KEY"]

# ATUALIZANDO ARQUIVO JSON NO GITHUB
g = Github(TOKEN_GITHUB) 

# repositorio
repo = g.get_repo("gabrielacaesar/wiki-calendar-scraper")

# local do arquivo no repositorio
contents = repo.get_contents("data/pt-content-01.json")

# atualizando arquivo 
repo.update_file(contents.path, 'Dados atualizados', get_events(janeiro, pt), contents.sha, branch="main")
print('5. Arquivo atualizado no GitHub')

print('--- FIM ---')
