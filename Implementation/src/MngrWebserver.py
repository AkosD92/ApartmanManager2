import os

from flask import Flask
from flask import render_template
from flask import url_for

TEMPLATE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + r'\templates'


print(TEMPLATE_DIR)
app = Flask(__name__, template_folder=TEMPLATE_DIR)

@app.route('/')
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)