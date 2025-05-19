from stats import count_words

def get_book_text(path):
    with open(path) as file:
        return file.read()
    
def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    print (f"{num_words} words found in the document")

main()
