

from jinja2 import StrictUndefined

from flask import Flask, render_template
# flash, jsonify, request, session, redirect

from flask_debugtoolbar import DebugToolbarExtension

# from model import db, connect_to_db, Character, Title, Episode, House
# from model import CharTitle, CharEp, CharHouse

# from search_queries import char_search_by_multiple_args, char_search_by_id
# from search_queries import char_search_by_house
# from search_queries import ep_search_by_id, title_search_by_id

# from api_queries import search_term_char_name, wikia_char_article_id, wikia_char_thumb
# from api_queries import char_page_etsy, char_page_ebay
# from api_queries import item_page_etsy, item_page_ebay

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
