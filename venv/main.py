from flask import Flask, request, render_template
from src import resume_manipulator

app = Flask(__name__, static_url_path="", static_folder="templates")
@app.route("/resume/generate", methods=["POST"])
def submit():
    form_data = {"name": request.form.get("id")}
    updated_resume = resume_manipulator.generate_resume(data=form_data)
    return updated_resume
@app.route("/")
def get_resume():
    resume_manipulator.generate_resume()
    return resume_manipulator.get_resume()

if __name__ == "__main__":
    resume_manipulator.generate_resume()
    app.run(host="localhost", port=8080, debug=True)
