from flask import render_template, Blueprint


notes_blueprint = Blueprint('notes_blueprint', __name__)


@notes_blueprint.route('/notes')
def notes():
    return render_template('notes.html')
