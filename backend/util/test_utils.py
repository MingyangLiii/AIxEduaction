import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
from model.database_connection import DatabaseConnection
from util.extract_table_of_content import *
from util.writer import *
from util.markdown_tag import *
from util.markdown_to_pdf import *


if __name__ == "__main__":
    config = get_config()
    path_output = config["base_dir"]+"/backend/data/output/"
    filename = "MPC.txt"


    db = DatabaseConnection()
    course_id = 544496
    textbook_id = 3299648

    course = db.get_course_by_id(course_id=course_id)
    # print(course.to_dict())
    text = ""
    text += h3(course.title)
    text+=line_break()
    text += div(course.description)
    text += seperator()


    textbook = db.get_textbook_by_id(course_id, textbook_id)
    text += div(textbook.title)
    text += line_break()
    text += div(textbook.preface)
    text += line_break()
    text += h4("目录")
    table = string_to_list(textbook.table)
    text += list(table)
    text += seperator()


    save_string_to_txt(path_output, filename, text)
    text = ""

    chapter_id_list = db.get_chapter_id_all_by_id(course_id, textbook_id)
    for chapter_id in chapter_id_list:
        chapter = db.get_chapter_by_id(course_id, textbook_id, chapter_id)

        text+=h4(chapter.title)
        text+=div(chapter.objective)
        text+=line_break()

        section_id_list = db.get_section_id_all_by_id(course_id, textbook_id, chapter_id)
        for section_id in section_id_list:
            section = db.get_section_by_id(course_id, textbook_id, chapter_id, section_id)
            text+=highlight(section.title)
            text+=line_break()
            text+=div(section.description)
            text+=div(section.example)
            text+=line_break()

        text+=line_break()
        text+=div(chapter.summary)
        text+=seperator()
        append_string_to_txt(path_output, filename, text)
        text = ""

    save_as_markdown(path_output+filename)
    # md_file = path_output + "react.md"
    # pdf_file = path_output + "react.pdf"
    # markdown_to_pdf(md_file, pdf_file)





