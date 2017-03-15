from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')
    color = request.args.get('color')
    print 'I like', color
    sql = "SELECT first_name, last_name, github FROM students where github=:github"
    cursor = hackbright.db.session.execute(sql, {'github': github})
    student = cursor.fetchone()

    # first, last, github = hackbright.get_student_by_github(github)
    return render_template("student_info.html", student=student)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-empty-form", methods=['GET'])
def get_add_new_student_form():
    """Show for for adding a new student."""

    return render_template("student_add.html")


@app.route("/student-add", methods=['POST'])
def add_new_student_info():
    """Adding new student info to page."""

    first = request.form.get("firstname")
    last = request.form.get("lastname")
    github = request.form.get("github")

    sql = """INSERT INTO students (first_name, last_name, github)
            VALUES (:first_name, :last_name, :github)"""

    hackbright.db.session.execute(sql,
                       {'first_name': first,
                        'last_name': last,
                         'github': github})

    hackbright.db.session.commit()

    return render_template('student_add_confirmation.html', first=first,
                            last=last, github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
