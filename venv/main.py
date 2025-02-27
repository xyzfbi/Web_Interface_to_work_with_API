from flask import Flask, request, jsonify
from src import resume_manipulator

app = Flask(__name__, static_url_path="", static_folder="templates")

@app.route("/resume/generate", methods=["POST"])
def generate_resume():
    data = request.get_json()
    resume_manipulator.generate_resume(data)
    return jsonify({"status": "success", "message": "Resume generated"})

@app.route("/")
def get_resume():
    resume_manipulator.generate_resume()
    return resume_manipulator.get_resume()

if __name__ == "__main__":
    resume_manipulator.generate_resume()
    app.run(host="localhost", port=8080, debug=True)