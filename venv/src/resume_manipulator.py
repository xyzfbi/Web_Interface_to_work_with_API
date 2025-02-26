from datetime import datetime
from jinja2 import Template


TEMPLATE_FILE_NAME = "./templates/index.html"
INDEX_FILE_NAME    = "./public/index.html"


def generate_resume(data=None  ):
    with open(TEMPLATE_FILE_NAME, "r", encoding="utf-8") as template_file:
        template_text = template_file.read()
        jinja_template = Template(template_text)
        default_data = {
            "name" : "Max",
            "job_position" : "Python Developer",
            "work_place" : "Yandex",
            "datetime" : datetime.now()
        }
        if data:
            default_data.update(data)

        rendered_resume = jinja_template.render(default_data)
        with open(INDEX_FILE_NAME, "w", encoding="utf-8") as resume_file:
            resume_file.write(rendered_resume)

def get_resume():
    with open(INDEX_FILE_NAME, "r") as resume_file:
        return resume_file.read()