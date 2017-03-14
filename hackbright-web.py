from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html", first=first,
                            last=last, github=github)
    return html


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

    sql = """INSERT INTO hackbright ()

    return render_template("student_add.html")


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
