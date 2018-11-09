from flask import Flask, render_template
from vsearch import search_for_letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search_for')
def do_search() -> str:
    return str(search_for_letters('life, the universe, and everything', 'eiru!'))

app.run()