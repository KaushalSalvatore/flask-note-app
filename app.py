from flask import Flask, render_template, request, redirect, url_for
from models import init_db, get_all_notes, add_note, delete_note, update_note

app = Flask(__name__)

@app.route('/')
def index():
    notes = get_all_notes()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add():
    content = request.form['content']
    add_note(content)
    return redirect(url_for('index'))

@app.route('/delete/<int:note_id>')
def delete(note_id):
    delete_note(note_id)
    return redirect(url_for('index'))

@app.route('/update/<int:note_id>', methods=['POST'])
def update(note_id):
    content = request.form['content']
    update_note(note_id, content)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
