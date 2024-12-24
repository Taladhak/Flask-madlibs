from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

# application factory function
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)


@app.route('/')
def ask_story():
    """Show list-of-stories form."""
    return render_template("select-story.html", stories=stories.values())

# HOME PAGE
@app.route('/questions')
def ask_questions():
    """Show homepage with list of stories"""
    story_id = request.args["story_id"]
    story = stories[story_id]
    prompts = story.prompts
    return render_template("questions.html", prompts=prompts, story_id=story_id)

# Story page
@app.route('/story')
def show_story():
    """Show story result."""
    story_id = request.args["story_id"]
    story = stories[story_id]    
    text = story.generate(request.args)
    return render_template("story.html", text=text, story_id=story_id)



