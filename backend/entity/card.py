class Card:
    def __init__(self, course_id=None, textbook_id=None, chapter_id=None, section_id=None, question=None, answer=None):
        self.course_id = course_id
        self.textbook_id = textbook_id
        self.chapter_id = chapter_id
        self.section_id = section_id
        self.question = question
        self.answer = answer

    def to_dict(self):
        return {
            'course_id': self.course_id,
            'textbook_id': self.textbook_id,
            'chapter_id': self.chapter_id,
            'section_id': self.section_id,
            'question':self.question,
            'answer':self.answer
        }