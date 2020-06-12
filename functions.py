def file_content_to_string(filename):
    """take a file and convert its text into a string"""
    with open(filename, "r") as f_object:
        str = f_object.read()
    return str

def concatenate(original, str):
    """concatenate a string to the left of a original string"""
    original = str + original
    return original

def get_word_and_definition(filename, dict):
    """ extract the word and their definitions rom en-es-en-Dic"""
    with open(filename, "r") as file_object:
        lines = file_object.readlines()

    i = 0
    j = len(lines)
    while i != j:
        if lines[i].strip() == "<w>":
            # the line after <w> is a word and after and the line after is its definition
            key = lines[i+1].strip()[3:-4].lower() # to lower
            value = lines[i+2].strip()[3:-4].lower()
            dict[key] = value

        i += 1

# could mix any and anyany into one function by simply adding src and dest parameters
def any(filename, dict):
    """ extract the word and their definitions from en-es-en-Dic files"""
    with open(filename, "r") as file_object:
        lines = file_object.readlines()

    i = 0
    j = len(lines)
    while i != j:
        if lines[i].strip() == "<tr>":
            # the line after <w> is a word and after and the line after is its definition
            key = lines[i+1].strip()[4:-5].lower() # to lower
            value = lines[i+2].strip()[4:-5].lower()
            dict[key] = value

        i += 1
def anyany(filename, dict):
    """ extract the word and their definitions from en-es-en-Dic files"""
    with open(filename, "r") as file_object:
        lines = file_object.readlines()

    i = 0
    j = len(lines)
    while i != j:
        if lines[i].strip() == "<td>":
            # the line after <w> is a word and after and the line after is its definition
            key = lines[i].strip()[4:-5].lower()  # to lower
            value = lines[i -1].strip()[4:-5].lower()
            dict[key] = value

        i += 1

def compare_dict(dict1, dict2):
    """Add the missing k,v from dict2 into dict1 by comparing the keys"""
    for k, v in dict2.items():
        if k not in dict1:
            dict1[k] = v