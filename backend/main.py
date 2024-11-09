import streamlit as st
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
from model.database_connection import DatabaseConnection
from entity.course import Course
from entity.chapter import Chapter
from entity.section import Section
from entity.textbook import Textbook

db = DatabaseConnection()

def course_store():
    """Display a list of courses to select from."""
    courses = db.get_course_all() 
    course_titles = [course.title for course in courses]
    
    selected_course = st.selectbox("Select a course:", course_titles)

    if selected_course:
        course = next(course for course in courses if course.title == selected_course)
        book_store(course.course_id)

def book_store(course_id):
    """Display a list of textbooks for the selected course."""
    textbooks = db.get_textbook_all_by_id(course_id)  
    textbook_titles = [textbook.title for textbook in textbooks]
    
    selected_textbook = st.selectbox("Select a textbook:", textbook_titles)
    

    if selected_textbook:
        textbook = next(textbook for textbook in textbooks if textbook.title == selected_textbook)
        textbook_page(course_id, textbook.textbook_id)

def textbook_page(course_id, textbook_id):
    """Display the chapters for the selected textbook."""
    chapters = db.get_chapter_all_by_id(course_id, textbook_id)  
    chapter_titles = [chapter.title for chapter in chapters]

    selected_chapter = st.selectbox("Select a chapter:", chapter_titles)
    
    if selected_chapter:
        chapter = next(chapter for chapter in chapters if chapter.title == selected_chapter)
        display_chapters_and_sections(course_id, textbook_id, chapter.chapter_id)

def display_chapters_and_sections(course_id, textbook_id, chapter_id):
    """Display sections for the selected chapter."""

    sections = db.get_section_all_by_id(course_id, textbook_id, chapter_id)
    section_titles = [section.title for section in sections]
    
    selected_section = st.selectbox("Select a section:", section_titles)
    

    if selected_section:
        section = next(section for section in sections if section.title == selected_section)
        st.write("Section Details:")
        st.write(f"Section Title: {section.title}")
        st.write(f"Section Description: {section.description}")


st.title("Course Store")
page = st.sidebar.selectbox("Select Page", ["Course Store"])

if page == "Course Store":
    course_store()