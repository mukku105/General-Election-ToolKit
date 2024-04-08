from flask import render_template, request, url_for, redirect
from app.routes.questions import bp
from app.extensions import db
from app.models.question import Question

@bp.route('/', methods=['GET', 'POST'])
def index():
    questions = Question.query.all()

    if request.method == 'POST':
        content = request.form.get('content')
        answer = request.form.get('answer')

        question = Question(content=content, answer=answer)
        db.session.add(question)
        db.session.commit()

        return redirect(url_for('archive/questions.index'))
    return render_template('archive/questions/index.html', questions=questions)