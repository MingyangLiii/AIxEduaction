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
from entity.card import Card
from util.generate_id import generate_id
from model.database_connection import DatabaseConnection



if __name__ == "__main__":
    db_conn = DatabaseConnection()
    """
    test course manipulation
    """
    ## Create a course
    # course_id = generate_id()
    # print(type(course_id))
    # course = Course(course_id=course_id, title="Test Course", description="Test Description")
    # db_conn.add_course(course)
    # print(f"Added course: {course.to_dict()}")

    # # Retrieve and verify the added course
    # retrieved_course = db_conn.get_course_by_id(course_id)
    # print(f"Retrieved course: {retrieved_course}")
    # assert retrieved_course.title == "Test Course", "Course retrieval failed."

    # # Update the course
    # course.title = "Updated Course Name"
    # db_conn.update_course_by_id(course_id, course)
    # updated_course = db_conn.get_course_by_id(course_id)
    # print(f"Updated course: {updated_course}")
    # assert updated_course.title == "Updated Course Name", "Course update failed."

    # # Remove the course
    # db_conn.remove_course_by_id(course_id)
    # removed_course = db_conn.get_course_by_id(course_id)
    # assert removed_course is None, "Course removal failed."
    # print(f"Course with ID {course_id} removed successfully.")



    """
    test textbook manipulation
    """

    # Create a textbook
    # course_id = generate_id()
    # textbook_id = generate_id()
    # textbook = Textbook(course_id=course_id, textbook_id=textbook_id, title="Test Textbook", preface="Test Preface", table="Test Table")
    # db_conn.add_textbook(textbook)
    # print(f"Added textbook: {textbook}")

    # # Retrieve and verify the added textbook
    # retrieved_textbook = db_conn.get_textbook_by_id(course_id, textbook_id)
    # print(f"Retrieved textbook: {retrieved_textbook}")
    # assert retrieved_textbook.title == "Test Textbook", "Textbook retrieval failed."

    # # Update the textbook
    # textbook.title = "Updated Textbook Title"
    # db_conn.update_textbook_by_id(course_id, textbook_id, textbook)
    # updated_textbook = db_conn.get_textbook_by_id(course_id, textbook_id)
    # print(f"Updated textbook: {updated_textbook}")
    # assert updated_textbook.title == "Updated Textbook Title", "Textbook update failed."

    # # Remove the textbook
    # db_conn.remove_textbook_by_id(course_id, textbook_id)
    # removed_textbook = db_conn.get_textbook_by_id(course_id, textbook_id)
    # assert removed_textbook is None, "Textbook removal failed."
    # print(f"Textbook with ID {textbook_id} removed successfully.")


    """
    test chapter manipulation
    """

    # # Create a chapter
    # course_id = generate_id()
    # textbook_id = generate_id()
    # chapter_id = generate_id()
    # chapter = Chapter(course_id=course_id, textbook_id=textbook_id, chapter_id=chapter_id, number=1, title="Test Chapter", objective="Test Objective", summary="Test Summary")
    # db_conn.add_chapter(chapter)
    # print(f"Added chapter: {chapter}")

    # # Retrieve and verify the added chapter
    # retrieved_chapter = db_conn.get_chapter_by_id(course_id, textbook_id, chapter_id)
    # print(f"Retrieved chapter: {retrieved_chapter}")
    # assert retrieved_chapter.title == "Test Chapter", "Chapter retrieval failed."

    # # Update the chapter
    # chapter.title = "Updated Chapter Title"
    # db_conn.update_chapter_by_id(course_id, textbook_id, chapter_id, chapter)
    # updated_chapter = db_conn.get_chapter_by_id(course_id, textbook_id, chapter_id)
    # print(f"Updated chapter: {updated_chapter}")
    # assert updated_chapter.title == "Updated Chapter Title", "Chapter update failed."

    # # Remove the chapter
    # db_conn.remove_chapter_by_id(course_id, textbook_id, chapter_id)
    # removed_chapter = db_conn.get_chapter_by_id(course_id, textbook_id, chapter_id)
    # assert removed_chapter is None, "Chapter removal failed."
    # print(f"Chapter with ID {chapter_id} removed successfully.")



    """
    test section manipulation
    """

    # Create a section
    # course_id = generate_id()
    # textbook_id = generate_id()
    # chapter_id = generate_id()
    # section_id = generate_id()
    # section = Section(course_id=course_id, textbook_id=textbook_id, chapter_id=chapter_id, section_id=section_id, number=1, title="Test Section", concept="Test Concept", description="Test Description", example="Test Example")
    # db_conn.add_section(section)
    # print(f"Added section: {section}")

    # Retrieve and verify the added section
    # retrieved_section = db_conn.get_section_by_id(course_id, textbook_id, chapter_id, section_id)
    # print(f"Retrieved section: {retrieved_section}")
    # assert retrieved_section.title == "Test Section", "Section retrieval failed."

    # Update the section
    # section.title = "Updated Section Title"
    # db_conn.update_section_by_id(course_id, textbook_id, chapter_id, section_id, section)
    # updated_section = db_conn.get_section_by_id(course_id, textbook_id, chapter_id, section_id)
    # print(f"Updated section: {updated_section}")
    # assert updated_section.title == "Updated Section Title", "Section update failed."

    # # Remove the section
    # db_conn.remove_section_by_id(course_id, textbook_id, chapter_id, section_id)
    # removed_section = db_conn.get_section_by_id(course_id, textbook_id, chapter_id, section_id)
    # assert removed_section is None, "Section removal failed."
    # print(f"Section with ID {section_id} removed successfully.")


    course_id = generate_id()
    card = Card(course_id=course_id, textbook_id="T001", chapter_id="CH001", section_id="S001", question="What is Python?", answer="A programming language.")
    db_conn.add_card(card)
    print(f"Added card: {card.to_dict()}")

    # Retrieve and verify the added card
    retrieved_card = db_conn.get_card_by_id(course_id, "T001", "CH001", "S001")
    print(f"Retrieved card: {retrieved_card}")
    assert retrieved_card.question == "What is Python?", "Card retrieval failed."

    # Update the card
    card.answer = "A powerful programming language."
    db_conn.update_card_by_id(course_id, "T001", "CH001", "S001", "What is Python?", card)
    updated_card = db_conn.get_card_by_id(course_id, "T001", "CH001", "S001")
    print(f"Updated card: {updated_card}")
    assert updated_card.answer == "A powerful programming language.", "Card update failed."

    # Remove the card
    db_conn.remove_card_by_id(course_id, "T001", "CH001", "S001", "What is Python?")
    removed_card = db_conn.get_card_by_id(course_id, "T001", "CH001", "S001")
    assert removed_card is None, "Card removal failed."
    print(f"Card with question 'What is Python?' removed successfully.")
