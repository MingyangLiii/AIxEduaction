import os

def save_string_to_txt(directory, filename, content):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = os.path.join(directory, filename)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"File saved to {file_path}")

def append_string_to_txt(directory, filename, content):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = os.path.join(directory, filename)
    
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Content appended to {file_path}")



def save_as_markdown(txt_file_path):
    if not os.path.isfile(txt_file_path):
        print(f"File {txt_file_path} does not exist.")
        return
    
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        content = txt_file.read()
    
    md_file_path = txt_file_path.replace('.txt', '.md')
    
    with open(md_file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(content)
    
    print(f"File has been saved as {md_file_path}")



