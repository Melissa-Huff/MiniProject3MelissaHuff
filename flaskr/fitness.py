# flaskr/fitness.py
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('fitness', __name__)

@bp.route('/')
@login_required
def index():
    db = get_db()
    activities = db.execute(
        'SELECT a.id, activity_type, date, duration, calories_burned, username'
        ' FROM activity a JOIN user u ON a.user_id = u.id'
        ' ORDER BY date DESC'
    ).fetchall()
    return render_template('fitness/index.html', activities=activities)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        activity_type = request.form['activity_type']
        date = request.form['date']
        duration = request.form['duration']
        calories_burned = request.form['calories_burned']
        error = None

        if not activity_type:
            error = 'Activity type is required.'

        if not date:
            error = 'Date is required.' if error is None else error

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO activity (user_id, date, activity_type, duration, calories_burned)'
                ' VALUES (?, ?, ?, ?, ?)',
                (g.user['id'], date, activity_type, duration, calories_burned)
            )
            db.commit()
            return redirect(url_for('fitness.index'))

    return render_template('fitness/create.html')
