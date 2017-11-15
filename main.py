__author__ = 'kathan'

import ujson
from entities import Sitter
from flask import Flask, render_template
app = Flask(__name__)

# Overriding jinja options because it clashes with angular
jinja_options = app.jinja_options.copy()
jinja_options.update(dict(
    block_start_string='<%',
    block_end_string='%>',
    variable_start_string='%%',
    variable_end_string='%%',
    comment_start_string='<#',
    comment_end_string='#>',
    cache_size=0
))

app.jinja_options = jinja_options

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/data/sitters', methods=['GET'])
def get_sitters():
    return ujson.dumps(Sitter.getSitters())

if __name__ == "__main__":
    app.run()