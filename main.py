#file_path = /home/user0/workspace/github.com/bootdev/bookbot/frankenstein.txt


def get_book_text(file_path):
    with open (file_path) as f:
        return f.read()
        

def main():
    path  = "books/frankenstein.txt"
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    


def count_words(text):
    words = text.split()
    return len(words)
        
   

    


main()








