from flask import Flask
from src import resume_manipulator

app = Flask(__name__, static_url_path="", static_folder="templates")
@app.route("/resume/generate", methods=["POST"])
@app.route("/")
def get_resume():
    resume_manipulator.generate_resume()
    return resume_manipulator.get_resume()

if __name__ == "__main__":
    resume_manipulator.generate_resume()
    app.run(host="localhost", port=8080, debug=True)
