def get_textbook_title(course_name):
    prompt = f"""
{course_name}
"""
    return prompt


def get_textbook_preface(course_name):
    prompt = f"""
{course_name}
"""
    return prompt


def get_textbook_table(course_name):
    prompt = f"""
{course_name}
"""
    return prompt




# Test 
def main():
    course_name = "deep learning"
    prompt = get_textbook_preface(course_name)
    print(prompt)


if __name__ == "__main__":
    main()