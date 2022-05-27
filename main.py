# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as read_file:
        file_contents_as_string = read_file.read()
    return file_contents_as_string

do = read_file_content("story.txt")
print(do)
 
    

new_dictionary = {}
def count_words():
    text = read_file_content("story.txt")
    split_the_text_into_a_list = text.split(" ")
    for word in split_the_text_into_a_list:
        make_the_list_a_dictionary_with_the_key_as_count = {word: split_the_text_into_a_list.count(word)}
        new_dictionary.update(make_the_list_a_dictionary_with_the_key_as_count)
    print(new_dictionary)

    

    # [assignment] Add your code here
count_words()
