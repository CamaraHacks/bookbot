#file_path = /home/user0/workspace/github.com/bootdev/bookbot/frankenstein.txt
from stats import count_words

def get_book_text(filepath):
    with open (filepath) as f:
        return f.read()


def main():
    path  = "books/frankenstein.txt"
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    
        

main()








