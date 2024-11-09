import ast
import re

def extract_table_of_content(input_string):
    start_index = input_string.index('[')
    end_index = input_string.rindex(']')
    list_str = input_string[start_index:end_index + 1]
    contents_list = ast.literal_eval(list_str)
    
    return contents_list


def list_to_string(lst):
    """Convert a simple Python list (e.g., strings/numbers) into a string."""
    return ','.join(map(str, lst))

def string_to_list(s):
    """Convert a string back into a simple Python list (e.g., strings/numbers)."""
    return s.split(',')

def get_string_between_quotes(text):
    match = re.search(r'\"(.*?)\"', text)
    if match:
        return match.group(1)
    return None