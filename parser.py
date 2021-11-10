import json
import os
from liquid import Environment, FileSystemLoader, Mode
from json import load

if __name__ == '__main__':
    app_path = os.path.dirname(os.path.realpath(__file__))
    data_file_path = os.path.join(app_path, 'data.json')
    if not os.path.exists(data_file_path):
        raise ValueError("Please provide a json 'data' file to populate the latex template")

    data_d = json.load(open(data_file_path))
    variable_delimiter = "##"

    env = Environment(
        statement_start_string=variable_delimiter,
        statement_end_string=variable_delimiter,
        loader=FileSystemLoader(""),
        tolerance=Mode.WARN)

    template = env.get_template("resume-test.templatex", globals=data_d)
    if not template:
        raise ValueError("Please provide a template file")
    render = template.render()
    print(render)
    with open('resume-test.tex', 'w') as file:
        file.write(render)
