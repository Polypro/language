import functions as f

# get file name of the books
b = f.file_content_to_string("book_list.txt")
book_files = b.split()


words = []
for book in book_files:
    # Add the words from a book into an array, then add it to words
    book = f.concatenate(book, "/home/bekind/language/books/")
    with open(book, "r") as f_object:
        content = f_object.read().split()
        words.append(content)




