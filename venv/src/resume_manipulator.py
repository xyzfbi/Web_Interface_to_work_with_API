from datetime import datetime
from jinja2 import Template
import json
import os

TEMPLATE_FILE_NAME = "./templates/index.html"
INDEX_FILE_NAME = "./public/index.html"
DATA_FILE_NAME = "./data/data.json"

def load_data():
    try:
        if not os.path.exists(DATA_FILE_NAME):
            raise FileNotFoundError

        with open(DATA_FILE_NAME, "r", encoding="utf-8") as json_file:
            content = json_file.read()
            print(f"Loaded JSON content: {content}")
            data = json.loads(content)
            print(f"Data loaded: {data}")
            return data
    except FileNotFoundError:
        default_data = {
            "name": "Max",
            "job_position": "Python Developer",
            "work_place": "Yandex",
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"File not found. Using default data: {default_data}")
        return default_data
    except json.JSONDecodeError as e:
        error_data = {
            "name": "Max",
            "job_position": "Python Developer",
            "work_place": "Yandex",
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"Error decoding JSON: {e}. Using default data: {error_data}")
        return error_data

def save_data(data):
    data["datetime"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Saving data: {data}")
    with open(DATA_FILE_NAME, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def generate_resume(data=None):
    if data:
        save_data(data)
    else:
        data = load_data()

    print(f"Generating resume with data: {data}")
    with open(TEMPLATE_FILE_NAME, "r", encoding="utf-8") as template_file:
        template_text = template_file.read()
        jinja_template = Template(template_text)
        rendered_resume = jinja_template.render(data)

        with open(INDEX_FILE_NAME, "w", encoding="utf-8") as resume_file:
            resume_file.write(rendered_resume)

def get_resume():
    with open(INDEX_FILE_NAME, "r", encoding="utf-8") as resume_file:
        return resume_file.read()