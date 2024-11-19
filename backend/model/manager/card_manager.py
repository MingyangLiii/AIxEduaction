import os
import sys
import pandas as pd

from entity.card import Card

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

class CardManager:
    def __init__(self, card_db):
        self.card_db = card_db

    def load_cards(self):
        """Load the cards from the CSV file into a pandas DataFrame."""
        if os.path.exists(self.card_db):
            df = pd.read_csv(self.card_db)
            if df.empty:
                print("Warning: The CSV file is empty. Returning an empty DataFrame.")
                return pd.DataFrame(columns=['course_id', 'textbook_id', 'chapter_id', 'section_id', 'question', 'answer'])
            return df
        else:
            return pd.DataFrame(columns=['course_id', 'textbook_id', 'chapter_id', 'section_id', 'question', 'answer'])

    def save_cards(self, df):
        """Save the cards DataFrame to the CSV file."""
        df.to_csv(self.card_db, index=False)

    def get_all_cards(self):
        """Retrieve all cards as a list of dictionaries."""
        df = self.load_cards()
        cards = []

        for _, row in df.iterrows():
            card = {
                'course_id': row['course_id'],
                'textbook_id': row['textbook_id'],
                'chapter_id': row['chapter_id'],
                'section_id': row['section_id'],
                'question': row['question'],
                'answer': row['answer']
            }
            cards.append(card)

        return cards

    def get_cards_by_id(self, course_id, textbook_id, chapter_id):
        """Retrieve all cards for a specific course, textbook, and chapter."""
        df = self.load_cards()

        df = df[
            (df['course_id'] == course_id) &
            (df['textbook_id'] == textbook_id) &
            (df['chapter_id'] == chapter_id)
        ]

        cards = []

        for _, row in df.iterrows():
            card = Card(
                course_id= row['course_id'],
                textbook_id= row['textbook_id'],
                chapter_id= row['chapter_id'],
                section_id= row['section_id'],
                question= row['question'],
                answer= row['answer']
            )
            cards.append(card)

        return cards

    def get_card_by_id(self, course_id, textbook_id, chapter_id, section_id):
        """Get a specific card by its course_id, textbook_id, chapter_id, and section_id."""
        df = self.load_cards()
        card_row = df[
            (df['course_id'] == course_id) &
            (df['textbook_id'] == textbook_id) &
            (df['chapter_id'] == chapter_id) &
            (df['section_id'] == section_id)
        ]
        
        if card_row.empty:
            return None  # Return None if card not found
        else:
            return Card(
                course_id= card_row['course_id'].values[0],
                textbook_id= card_row['textbook_id'].values[0],
                chapter_id= card_row['chapter_id'].values[0],
                section_id= card_row['section_id'].values[0],
                question= card_row['question'].values[0],
                answer= card_row['answer'].values[0]
            )


    def add_card(self, card):
        """Add a card to the DataFrame and save to the CSV file if it does not already exist."""
        df = self.load_cards()

        if df.empty:
            df = pd.DataFrame(columns=['course_id', 'textbook_id', 'chapter_id', 'section_id', 'question', 'answer'])

        if df[
            (df['course_id'] == card.course_id) &
            (df['textbook_id'] == card.textbook_id) &
            (df['chapter_id'] == card.chapter_id) &
            (df['section_id'] == card.section_id) &
            (df['question'] == card.question)
        ].any(axis=None):
            print(f"Card with question '{card.question}' already exists.")
            return False

        # Create a new DataFrame for the new card
        new_card_row = pd.DataFrame({
            'course_id': [card.course_id],
            'textbook_id': [card.textbook_id],
            'chapter_id': [card.chapter_id],
            'section_id': [card.section_id],
            'question': [card.question],
            'answer': [card.answer]
        })

        # Append the new card to the existing DataFrame
        df = pd.concat([df, new_card_row], ignore_index=True)

        # Save the updated DataFrame back to the CSV
        self.save_cards(df)
        print(f"Card with question '{card.question}' added successfully.")
        return True

    def add_card_list(self, card_list):
        """Add multiple cards to the DataFrame and save to the CSV file if they do not already exist."""
        df = self.load_cards()

        if df.empty:
            df = pd.DataFrame(columns=['course_id', 'textbook_id', 'chapter_id', 'section_id', 'question', 'answer'])

        cards_added = 0
        for card in card_list:
            # Check if the card already exists
            if df[
                (df['course_id'] == card.course_id) &
                (df['textbook_id'] == card.textbook_id) &
                (df['chapter_id'] == card.chapter_id) &
                (df['section_id'] == card.section_id) &
                (df['question'] == card.question)
            ].any(axis=None):
                print(f"Card with question '{card.question}' already exists. Skipping.")
                continue

            # Create a new DataFrame for the new card
            new_card_row = pd.DataFrame({
                'course_id': [card.course_id],
                'textbook_id': [card.textbook_id],
                'chapter_id': [card.chapter_id],
                'section_id': [card.section_id],
                'question': [card.question],
                'answer': [card.answer]
            })

            # Append the new card to the existing DataFrame
            df = pd.concat([df, new_card_row], ignore_index=True)
            cards_added += 1

        if cards_added > 0:
            # Save the updated DataFrame back to the CSV only if new cards were added
            self.save_cards(df)
            print(f"{cards_added} cards added successfully.")
        else:
            print("No new cards were added as they already exist.")

        return cards_added > 0

    def update_card_by_id(self, course_id, textbook_id, chapter_id, section_id, question, card):
        """Update a card's details by its course_id, textbook_id, chapter_id, section_id, and question."""
        df = self.load_cards()

        # Check if the card exists
        if df[
            (df['course_id'] == course_id) &
            (df['textbook_id'] == textbook_id) &
            (df['chapter_id'] == chapter_id) &
            (df['section_id'] == section_id) &
            (df['question'] == question)
        ].any(axis=None):
            # Update the relevant fields
            df.loc[
                (df['course_id'] == course_id) &
                (df['textbook_id'] == textbook_id) &
                (df['chapter_id'] == chapter_id) &
                (df['section_id'] == section_id) &
                (df['question'] == question),
                ['answer']
            ] = [card.answer]
            
            self.save_cards(df)
            print(f"Card with question '{question}' updated successfully.")
            return True
        else:
            print(f"No card with question '{question}' found.")
            return False

    def remove_card_by_id(self, course_id, textbook_id, chapter_id, section_id, question):
        """Remove a card by its course_id, textbook_id, chapter_id, section_id, and question."""
        df = self.load_cards()

        if df.empty:
            print(f"No cards to remove. The file {self.card_db} is empty.")
            return False

        # Check if the card with the given ID exists
        if not df[
            (df['course_id'] == course_id) &
            (df['textbook_id'] == textbook_id) &
            (df['chapter_id'] == chapter_id) &
            (df['section_id'] == section_id) &
            (df['question'] == question)
        ].any(axis=None):
            print(f"Card with question '{question}' does not exist.")
            return False

        # Remove the card from the DataFrame
        df = df[
            (df['course_id'] != course_id) |
            (df['textbook_id'] != textbook_id) |
            (df['chapter_id'] != chapter_id) |
            (df['section_id'] != section_id) |
            (df['question'] != question)
        ]

        # Save the updated DataFrame back to the CSV
        self.save_cards(df)
        print(f"Card with question '{question}' has been removed successfully.")
        return True



