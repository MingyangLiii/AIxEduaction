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
from util.extract_table_of_content import get_string_between_quotes
from util.markdown_tag import highlight

db = DatabaseConnection()

# Textbook Display Section

def select_page():
    pages = ["Book Store", "Schedule", "Todo List", "Review", "Other"]
    selected_page = st.sidebar.selectbox("Select a space:", pages)
    if selected_page:
        return selected_page
    return None

def select_course():
    """Display a list of courses to select from in the sidebar."""
    st.sidebar.title("Course Selection")
    courses = db.get_course_all()
    course_titles = [course.title for course in courses]
    
    selected_course_title = st.sidebar.selectbox("Select a course:", course_titles)
    if selected_course_title:
        return next(course for course in courses if course.title == selected_course_title)
    return None

def select_textbook(course_id):
    """Display a list of textbooks for the selected course in the sidebar."""
    textbooks = db.get_textbook_all_by_id(course_id)
    textbook_titles = [textbook.title for textbook in textbooks]
    
    selected_textbook_title = st.sidebar.selectbox("Select a textbook:", textbook_titles)
    if selected_textbook_title:
        return next(textbook for textbook in textbooks if textbook.title == selected_textbook_title)
    return None


def select_chapter(course_id, textbook_id):
    """Display a list of chapters for the selected textbook."""
    chapters = db.get_chapter_all_by_id(course_id, textbook_id)
    chapter_titles = [chapter.title for chapter in chapters]
    
    selected_chapter_title = st.selectbox("Select a chapter:", chapter_titles)
    if selected_chapter_title:
        return next(chapter for chapter in chapters if chapter.title == selected_chapter_title)
    return None

def select_section(course_id, textbook_id, chapter_id):
    """Display a list of sections for the selected chapter."""
    sections = db.get_section_all_by_id(course_id, textbook_id, chapter_id)
    section_titles = [section.title for section in sections]
    
    selected_section_title = st.selectbox("Select a section:", section_titles)
    if selected_section_title:
        return next(section for section in sections if section.title == selected_section_title)
    return None

def display_section_details(section):
    """Display details of the selected section."""
    st.write(f"**{section.title}**")
    st.write(f"{section.description}")
    st.write(f"{section.example}")


# Todo List Section

def todo_list_app():
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    def add_task():
        task = st.session_state.new_task
        if task:  
            st.session_state.tasks.append(task)
            st.session_state.new_task = "" 

    st.title("📝 To-Do List")
    st.write("**Manage your tasks efficiently!**")

    st.text_input("Add a new task", key="new_task", on_change=add_task)

    tasks_to_remove = []
    for i, task in enumerate(st.session_state.tasks):
        if st.checkbox(task, key=f"task_{i}"):
            tasks_to_remove.append(i) 
    
    if tasks_to_remove:
        for index in reversed(sorted(tasks_to_remove)):
            st.session_state.tasks.pop(index)



# Main Loop

selected_course = select_course()
if selected_course:
    selected_textbook = select_textbook(selected_course.course_id)
    if selected_textbook:
        selected_page = select_page()
        if selected_page == "Book Store":
            st.title("📚 Book Store")
            st.write(selected_textbook.title)
            selected_chapter = select_chapter(selected_course.course_id, selected_textbook.textbook_id)
            if selected_chapter:
                selected_section = select_section(selected_course.course_id, selected_textbook.textbook_id, selected_chapter.chapter_id)
                if selected_section:
                    display_section_details(selected_section)
        
        elif selected_page == "Schedule":
            st.title("🗓️ Schedule")
            st.write(highlight(get_string_between_quotes(selected_course.title)))
        
        elif selected_page == "Todo List":
            todo_list_app()

        elif selected_page == "Review":
            st.title("🪧 Review")
            st.write(highlight(get_string_between_quotes(selected_course.title)))
        else:
            st.title("Other")
