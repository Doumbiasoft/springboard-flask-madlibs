from flask import Flask,request,render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] ="IamMouhamedDoumbia86"
debug=DebugToolbarExtension(app)

@app.route('/')
def index():
    story_params = story.prompts
    return render_template('index.html',story_params=story_params)

@app.route('/story')
def the_story():
    the_story = story.generate(request.args)
    return render_template('story.html',the_story=the_story)