from flask import Flask, render_template, url_for, flash, redirect
from myForms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5b930b141aa659fc8bcc08a37957e1db'

latestForum = {
    'title': "New entry from the forum",
    'content': "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                "Phasellus ut leo in lorem ultricies lacinia. In auctor urna eget nisl fermentum,"
                "faucibus consequat leo sollicitudin. Duis ut dignissim erat, et posuere eros. Vivamus eget vehicula eros."
                "Nulla ultrices orci quam, at suscipit sem tempor vel. Curabitur convallis viverra vestibulum."
}

latestQuestion = {
    'title': "New entry from the questions",
    'content': "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    "Phasellus ut leo in lorem ultricies lacinia. In auctor urna eget nisl fermentum,"
                    "faucibus consequat leo sollicitudin. Duis ut dignissim erat, et posuere eros. Vivamus eget vehicula eros."
                    "Nulla ultrices orci quam, at suscipit sem tempor vel. Curabitur convallis viverra vestibulum." 
}
   

#Allow GET and POST function callbacks
@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = LoginForm()
    return render_template('index.html', latestForum=latestForum, latestQuestion=latestQuestion, form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # What to display on successful bootstrap message
        flash(f"Account created for {form.username.data}", "success")
        return redirect(url_for('home'))
    return render_template('register.html', form=form)
