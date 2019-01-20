from flask import Flask, render_template, url_for
app = Flask(__name__)

latestForum = {
        'title' : "New entry from the forum",
        'content' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    "Phasellus ut leo in lorem ultricies lacinia. In auctor urna eget nisl fermentum,"
                    "faucibus consequat leo sollicitudin. Duis ut dignissim erat, et posuere eros. Vivamus eget vehicula eros."
                    "Nulla ultrices orci quam, at suscipit sem tempor vel. Curabitur convallis viverra vestibulum." 
}

latestQuestion = {
        'title' : "New entry from the questions",
        'content' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    "Phasellus ut leo in lorem ultricies lacinia. In auctor urna eget nisl fermentum,"
                    "faucibus consequat leo sollicitudin. Duis ut dignissim erat, et posuere eros. Vivamus eget vehicula eros."
                    "Nulla ultrices orci quam, at suscipit sem tempor vel. Curabitur convallis viverra vestibulum." 
}
   


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', latestForum=latestForum, latestQuestion=latestQuestion)