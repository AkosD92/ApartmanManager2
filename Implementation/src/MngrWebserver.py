import os

from flask import Flask
from flask import render_template

TEMPLATE_DIR = os.path.abspath('./templates')

print(TEMPLATE_DIR)

app = Flask(__name__, template_folder=TEMPLATE_DIR)

@app.route('/')
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=False)