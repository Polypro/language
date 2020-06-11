def file_content_to_string(filename):
    """take a file and convert its text into a string"""
    with open(filename, "r") as f_object:
        str = f_object.read()
    return str

def concatenate(original, str):
    """concatenate a string to the left of a original string"""
    original = str + original
    return original