import os
import sys
import pandas as pd
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from entity.section import Section

class SectionManager:
    def __init__(self, section_db):
        self.section_db = section_db

    def load_section(self):
        """Load the sections from the CSV file into a pandas DataFrame."""
        if os.path.exists(self.section_db):
            df = pd.read_csv(self.section_db)
            if df.empty:
                print("Warning: The CSV file is empty. Returning an empty DataFrame.")
                return pd.DataFrame(columns=['course_id', 'textbook_id', 'chapter_id', 'section_id', 'number', 'title', 'concept', 'description', 'example'])
            return df
        else:
            return pd.DataFrame(columns=['course_id', 'textbook_id', 'chapter_id', 'section_id', 'number', 'title', 'concept', 'description', 'example'])

    def save_section(self, df):
        """Save the sections DataFrame to the CSV file."""
        df.to_csv(self.section_db, index=False)

    def get_section_all(self):
        """Retrieve all sections as a list of Section objects."""
        df = self.load_section()
        sections = []

        for _, row in df.iterrows():
            section = Section(
                course_id=row['course_id'],
                textbook_id=row['textbook_id'],
                chapter_id=row['chapter_id'],
                section_id=row['section_id'],
                number=row['number'],
                title=row['title'],
                concept=row['concept'],
                description=row['description'],
                example=row['example']
            )
            sections.append(section)

        return sections

    def get_section_all_by_id(self, course_id, textbook_id, chapter_id):
        """Retrieve all sections as a list of Section objects."""
        df = self.load_section()

        df = section_row = df[
            (df['course_id'] == course_id) &
            (df['textbook_id'] == textbook_id) &
            (df['chapter_id'] == chapter_id)
        ]

        sections = []

        for _, row in df.iterrows():
            section = Section(
                course_id=row['course_id'],
                textbook_id=row['textbook_id'],
                chapter_id=row['chapter_id'],
                section_id=row['section_id'],
                number=row['number'],
                title=row['title'],
                concept=row['concept'],
                description=row['description'],
                example=row['example']
            )
            sections.append(section)

        return sections

    def get_section_by_id(self, course_id, textbook_id, chapter_id, section_id):
        """Get a specific section by its course_id, textbook_id, chapter_id, and section_id."""
        df = self.load_section()
        section_row = df[
            (df['course_id'] == course_id) &
            (df['textbook_id'] == textbook_id) &
            (df['chapter_id'] == chapter_id) &
            (df['section_id'] == section_id)
        ]
        
        if section_row.empty:
            return None  # Return None if section not found
        else:
            return Section(
                course_id=section_row['course_id'].values[0],
                textbook_id=section_row['textbook_id'].values[0],
                chapter_id=section_row['chapter_id'].values[0],
                section_id=section_row['section_id'].values[0],
                number=section_row['number'].values[0],
                title=section_row['title'].values[0],
                concept=section_row['concept'].values[0],
                description=section_row['description'].values[0],
                example=section_row['example'].values[0]
            )

    def get_section_id_all_by_id(self, course_id, textbook_id, chapter_id):
        """Retrieve all section_ids for a given course, textbook, and chapter."""
        df = self.load_section()

        if df.empty:
            print("Warning: No sections found. Returning an empty list.")
            return []

        section_ids = df[
            (df['course_id'] == course_id) &
            (df['textbook_id'] == textbook_id) &
            (df['chapter_id'] == chapter_id)
        ]['section_id'].tolist()
        
        return section_ids

    def add_section(self, section):
        """Add a section to the DataFrame and save to the CSV file if it does not already exist."""
        df = self.load_section()

        if df.empty:
            df = pd.DataFrame(columns=['course_id', 'textbook_id', 'chapter_id', 'section_id', 'number', 'title', 'concept', 'description', 'example'])

        if df[
            (df['course_id'] == section.course_id) &
            (df['textbook_id'] == section.textbook_id) &
            (df['chapter_id'] == section.chapter_id) &
            (df['section_id'] == section.section_id)
        ].any(axis=None):
            print(f"Section with ID {section.section_id} already exists.")
            return False

        # Create a new DataFrame for the new section
        new_section_row = pd.DataFrame({
            'course_id': [section.course_id],
            'textbook_id': [section.textbook_id],
            'chapter_id': [section.chapter_id],
            'section_id': [section.section_id],
            'number': [section.number],
            'title': [section.title],
            'concept': [section.concept],
            'description': [section.description],
            'example': [section.example]
        })

        # Append the new section to the existing DataFrame
        df = pd.concat([df, new_section_row], ignore_index=True)

        # Save the updated DataFrame back to the CSV
        self.save_section(df)
        print(f"Section with ID {section.section_id} added successfully.")
        return True
    
    def add_section_list(self, section_list):
        """Add multiple sections to the DataFrame and save to the CSV file if they do not already exist."""
        df = self.load_section()

        if df.empty:
            df = pd.DataFrame(columns=['course_id', 'textbook_id', 'chapter_id', 'section_id', 'number', 'title', 'concept', 'description', 'example'])

        sections_added = 0
        for section in section_list:
            # Check if the section already exists
            if df[
                (df['course_id'] == section.course_id) &
                (df['textbook_id'] == section.textbook_id) &
                (df['chapter_id'] == section.chapter_id) &
                (df['section_id'] == section.section_id)
            ].any(axis=None):
                print(f"Section with ID {section.section_id} already exists. Skipping.")
                continue

            # Create a new DataFrame for the new section
            new_section_row = pd.DataFrame({
                'course_id': [section.course_id],
                'textbook_id': [section.textbook_id],
                'chapter_id': [section.chapter_id],
                'section_id': [section.section_id],
                'number': [section.number],
                'title': [section.title],
                'concept': [section.concept],
                'description': [section.description],
                'example': [section.example]
            })

            # Append the new section to the existing DataFrame
            df = pd.concat([df, new_section_row], ignore_index=True)
            sections_added += 1

        if sections_added > 0:
            # Save the updated DataFrame back to the CSV only if new sections were added
            self.save_section(df)
            print(f"{sections_added} sections added successfully.")
        else:
            print("No new sections were added as they already exist.")

        return sections_added > 0


    def update_section_by_id(self, course_id, textbook_id, chapter_id, section_id, section):
        """Update a section's details by its course_id, textbook_id, chapter_id, and section_id."""
        df = self.load_section()

        # Check if the section exists
        if df[
            (df['course_id'] == course_id) &
            (df['textbook_id'] == textbook_id) &
            (df['chapter_id'] == chapter_id) &
            (df['section_id'] == section_id)
        ].any(axis=None):
            # Update the relevant fields
            df.loc[
                (df['course_id'] == course_id) &
                (df['textbook_id'] == textbook_id) &
                (df['chapter_id'] == chapter_id) &
                (df['section_id'] == section_id),
                ['number', 'title', 'concept', 'description', 'example']
            ] = [section.number, section.title, section.concept, section.description, section.example]
            
            self.save_section(df)
            print(f"Section with ID {section_id} updated successfully.")
            return True
        else:
            print(f"No section with ID {section_id} found.")
            return False

    def remove_section_all(self):
        """Remove all sections from the CSV file."""
        df = self.load_section()

        if df.empty:
            print("No sections to remove. The file is already empty.")
            return False

        # Create an empty DataFrame with the same columns
        empty_df = pd.DataFrame(columns=['course_id', 'textbook_id', 'chapter_id', 'section_id', 'number', 'title', 'concept', 'description', 'example'])
        
        # Save the empty DataFrame back to the CSV file
        self.save_section(empty_df)
        print("All sections have been removed successfully.")
        return True

    def remove_section_by_id(self, course_id, textbook_id, chapter_id, section_id):
        """Remove a section by its course_id, textbook_id, chapter_id, and section_id."""
        df = self.load_section()

        if df.empty:
            print(f"No sections to remove. The file {self.section_db} is empty.")
            return False

        # Check if the section with the given ID exists
        if not df[
            (df['course_id'] == course_id) &
            (df['textbook_id'] == textbook_id) &
            (df['chapter_id'] == chapter_id) &
            (df['section_id'] == section_id)
        ].any(axis=None):
            print(f"Section with ID {section_id} does not exist.")
            return False

        # Remove the section from the DataFrame
        df = df[
            (df['course_id'] != course_id) |
            (df['textbook_id'] != textbook_id) |
            (df['chapter_id'] != chapter_id) |
            (df['section_id'] != section_id)
        ]

        # Save the updated DataFrame back to the CSV
        self.save_section(df)
        print(f"Section with ID {section_id} has been removed successfully.")
        return True


