

from jinja2 import StrictUndefined

from flask import Flask, render_template

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.secret_key = "SEEKRIT"

app.jinja_env.undefined = StrictUndefined

###########################################
# Main routes


@app.route('/')
def index():
    """Index."""

    return render_template("index.html")


@app.route('/techskills')
def techskills():
    """Tech Skills"""

    return render_template("techskillsmain.html")


@app.route('/education')
def education():
    """Education"""

    return render_template("educationmain.html")


@app.route('/projects')
def projects():
    """Projects"""

    return render_template("projectsmain.html")


@app.route('/resume')
def resume():
    """Resume"""

    return render_template("resumemain.html")


@app.route('/extracurricular')
def extracurricular():
    """Extra Curricular"""

    return render_template("extracurricularmain.html")


###########################################
# Helper functions

if __name__ == "__main__":

    app.debug = True
    app.jinja_env.auto_reload = app.debug

    # connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
