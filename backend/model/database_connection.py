import os
import sys
import pandas as pd
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
from entity.course import Course
from entity.chapter import Chapter
from entity.section import Section
from entity.textbook import Textbook
from util.generate_id import generate_id
from model.manager.course_manager import CourseManager
from model.manager.textbook_manager import TextbookManager
from model.manager.chapter_manager import ChapterManager
from model.manager.section_manager import SectionManager

class DatabaseConnection:
    def __init__(self):
        self.base_dir = get_config()["base_dir"] + "/backend/data/database"
        self.course_db = self.base_dir + "/course.csv"
        self.textbook_db = self.base_dir + "/textbook.csv"
        self.chapter_db = self.base_dir + "/chapter.csv"
        self.section_db = self.base_dir + "/section.csv"

        self.course_manager = CourseManager(self.course_db)
        self.textbook_manager = TextbookManager(self.textbook_db)
        self.chapter_manager = ChapterManager(self.chapter_db)
        self.section_manager = SectionManager(self.section_db)



    def load_course(self):
        """Load the courses from the CSV file into a pandas DataFrame."""
        return self.course_manager.load_course()

    def save_course(self, df):
        """Save the courses DataFrame to the CSV file."""
        self.course_manager.save_course(df)

    def get_course_by_id(self, course_id):
        """Get a specific course by its course_id."""
        return self.course_manager.get_course_by_id(course_id)

    def get_course_all(self):
        """Retrieve all courses from the CSV file as a list of Course objects."""
        return self.course_manager.get_course_all()

    def get_course_id_all(self):
        """Retrieve all course IDs from the CSV file as a list."""
        return self.course_manager.get_course_id_all()

    def add_course(self, course):
        """Add a course to the DataFrame and save to the CSV file if it does not already exist."""
        return self.course_manager.add_course(course)

    def remove_course_by_id(self, course_id):
        """Remove a course by its course_id and update the CSV file."""
        return self.course_manager.remove_course_by_id(course_id)

    def update_course_by_id(self, course_id, course):
        """Update a course's title and/or description by its course_id."""
        return self.course_manager.update_course_by_id(course_id, course)

    def remove_course_all(self):
        """Remove all courses from the CSV file."""
        return self.course_manager.remove_course_all()




    def get_textbook_by_id(self, course_id, textbook_id):
        """Get a specific textbook by its course_id and textbook_id."""
        return self.textbook_manager.get_textbook_by_id(course_id, textbook_id)

    def get_textbook_all_by_id(self, course_id):
        """Retrieve all textbooks for a specific course_id as a list of Textbook objects."""
        return self.textbook_manager.get_textbook_all_by_id(course_id)

    def get_textbook_all(self):
        """Retrieve all textbooks from the CSV file as a list of dictionaries."""
        return self.textbook_manager.get_textbook_all()

    def get_textbook_id_all_by_id(self, course_id):
        """Retrieve all textbook IDs for a specific course_id."""
        return self.textbook_manager.get_textbook_id_all_by_id(course_id)

    def add_textbook(self, textbook):
        """Add a textbook to the DataFrame and save to the CSV file if it does not already exist."""
        return self.textbook_manager.add_textbook(textbook)

    def remove_textbook_all_by_id(self, course_id):
        """Remove all textbooks for a specific course_id and update the CSV file."""
        return self.textbook_manager.remove_textbook_all_by_course_id(course_id)

    def remove_textbook_by_id(self, course_id, textbook_id):
        """Remove a textbook by its course_id and textbook_id and update the CSV file."""
        return self.textbook_manager.remove_textbook_by_id(course_id, textbook_id)

    def remove_textbook_all(self):
        """Remove all textbooks from the CSV file."""
        return self.textbook_manager.remove_textbook_all()

    def update_textbook_by_id(self, course_id, textbook_id, new_textbook):
        """Update the details of a specific textbook by course_id and textbook_id."""
        return self.textbook_manager.update_textbook_by_id(course_id, textbook_id, new_textbook)
    




    def load_chapter(self):
        """Delegate the loading of chapters to the chapter manager."""
        return self.chapter_manager.load_chapter()

    def save_chapter(self, df):
        """Delegate saving the chapters to the chapter manager."""
        self.chapter_manager.save_chapter(df)

    def get_chapter_all(self):
        """Delegate retrieval of all chapters to the chapter manager."""
        return self.chapter_manager.get_chapter_all()

    def get_chapter_by_id(self, course_id, textbook_id, chapter_id):
        """Delegate retrieval of a chapter by its course_id, textbook_id, and chapter_id to the chapter manager."""
        return self.chapter_manager.get_chapter_by_id(course_id, textbook_id, chapter_id)

    def get_chapter_all_by_id(self, course_id, textbook_id):
        """Delegate retrieval of all chapters by course_id and textbook_id to the chapter manager."""
        return self.chapter_manager.get_chapter_all_by_id(course_id, textbook_id)

    def get_chapter_id_all_by_id(self, course_id, textbook_id):
        """Delegate retrieval of all chapter IDs to the chapter manager."""
        return self.chapter_manager.get_chapter_id_all_by_id(course_id, textbook_id)

    def add_chapter(self, chapter):
        """Delegate adding a chapter to the chapter manager."""
        return self.chapter_manager.add_chapter(chapter)

    def update_chapter_by_id(self, course_id, textbook_id, chapter_id, updated_chapter):
        """Delegate updating a chapter by course_id, textbook_id, and chapter_id to the chapter manager."""
        return self.chapter_manager.update_chapter_by_id(course_id, textbook_id, chapter_id, updated_chapter)

    def remove_chapter_all(self):
        """Delegate removal of all chapters to the chapter manager."""
        return self.chapter_manager.remove_chapter_all()

    def remove_chapter_all_by_course_textbook_id(self, course_id, textbook_id):
        """Delegate removal of all chapters by course_id and textbook_id to the chapter manager."""
        return self.chapter_manager.remove_chapter_all_by_course_textbook_id(course_id, textbook_id)

    def remove_chapter_by_id(self, course_id, textbook_id, chapter_id):
        """Delegate removal of a chapter by course_id, textbook_id, and chapter_id to the chapter manager."""
        return self.chapter_manager.remove_chapter_by_id(course_id, textbook_id, chapter_id)
    


    def load_section(self):
        """Delegate loading sections to the section manager."""
        return self.section_manager.load_section()

    def save_section(self, df):
        """Delegate saving sections to the section manager."""
        self.section_manager.save_section(df)

    def get_section_all(self):
        """Delegate retrieval of all sections to the section manager."""
        return self.section_manager.get_section_all()
    
    def get_section_all_by_id(self, course_id, textbook_id, chapter_id):
        return self.section_manager.get_section_all_by_id(course_id, textbook_id, chapter_id)

    def get_section_by_id(self, course_id, textbook_id, chapter_id, section_id):
        """Delegate retrieval of a section by its course_id, textbook_id, chapter_id, and section_id to the section manager."""
        return self.section_manager.get_section_by_id(course_id, textbook_id, chapter_id, section_id)

    def get_section_id_all_by_id(self, course_id, textbook_id, chapter_id):
        """Delegate retrieval of all section_ids by course_id, textbook_id, and chapter_id to the section manager."""
        return self.section_manager.get_section_id_all_by_id(course_id, textbook_id, chapter_id)

    def add_section(self, section):
        """Delegate adding a section to the section manager."""
        return self.section_manager.add_section(section)

    def update_section_by_id(self, course_id, textbook_id, chapter_id, section_id, section):
        """Delegate updating a section by course_id, textbook_id, chapter_id, and section_id to the section manager."""
        return self.section_manager.update_section_by_id(course_id, textbook_id, chapter_id, section_id, section)

    def remove_section_all(self):
        """Delegate removal of all sections to the section manager."""
        return self.section_manager.remove_section_all()

    def remove_section_by_id(self, course_id, textbook_id, chapter_id, section_id):
        """Delegate removal of a section by course_id, textbook_id, chapter_id, and section_id to the section manager."""
        return self.section_manager.remove_section_by_id(course_id, textbook_id, chapter_id, section_id)


    
