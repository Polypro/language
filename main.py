# This a language game similar to duolingo but it has more content so it is less repetitive
import functions as f
from googletrans import Translator

# get file name of the books
b = f.file_content_to_string("book_list.txt")
book_files = b.split()

words = []
for filename in book_files:
    # Add the words from a book into an array, then add it to words
    filename = f.concatenate(filename, "/home/bekind/language/books/")
    with open(filename, "r") as f_object:
        content = f_object.read().split()
        words.append(content)

# # could use json on that
# # find the frequency of each words (includes some english words
# freq = {}
# for List in words:
#     for word in List:
#         if word.lower() in freq.keys():
#             freq[word.lower()] += 1
#         elif word.lower() not in freq.keys():
#             freq[word.lower()] = 1
#
# count = 0
# for k,v in freq.items():
#     if v > 100:
#         count += 1
#         print(k)
#     #print(k, ":", v)
# print(count)

#----------------------------------
#create translation dictionnaries
#----------------------------------
dict_en_es = {}
dict_es_en = {}
filenames_EN_ES = ["translator-files/en-es-en-Dic/src/main/resources/dic/verbs/en-es.xml",
                   "translator-files/en-es-en-Dic/src/main/resources/dic/en-es.xml"]
filenames_ES_EN = ["translator-files/en-es-en-Dic/src/main/resources/dic/verbs/es-en.xml",
                   "translator-files/en-es-en-Dic/src/main/resources/dic/es-en.xml"]

for filename in filenames_EN_ES:
    f.get_word_and_definition(filename, dict_en_es)
for filename in filenames_ES_EN:
    f.get_word_and_definition(filename, dict_es_en)

#compare two dict and add those missing to source
perhaps_extra = {}
f.any("en-es-top-92-verbs.txt", perhaps_extra)
f.compare_dict(dict_en_es, perhaps_extra)

perhaps_extra = {}
f.any("en-es-top-92-verbs.txt", perhaps_extra)
f.compare_dict(dict_es_en, perhaps_extra)
# to delete
for k, v in dict_en_es.items():
    print(k, ":", v)
#---------------------------------
# game creation TODO
#---------------------------------
# get expressions
    # could check if value is a string containing more that 2 words
    # that would mean it is a full sentence
    # could write that in a json file
for k, v in dict_en_es.items():
    for char in k:
        if char.isalpha() == False and char != "/":
            print("-----", k, "---", v)
            break



