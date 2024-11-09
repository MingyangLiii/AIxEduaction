def h1(text):
    return "# "+ text + "\n\n"

def h2(text):
    return "## "+ text + "\n\n"

def h3(text):
    return "### "+ text + "\n\n"

def h4(text):
    return "### "+ text + "\n\n"

def page_break():
    return "\pagebreak\n\n"

def line_break():
    return "\n\n"

def div(text):
    return text + "\n\n"

def list(element_list):
    output = ""
    for elem in element_list:
        output += elem + "\n"
    output += "\n\n"
    return output

def highlight(text):
    return f"**{text}** \n\n"

def seperator():
    return "\n\n\n\n---\n\n\n\n"

