def main():
    path ="/home/nandu/workspace/github.com/nandunagesh123/bookbot/books/frankenstein.txt"
    text=get_book_text(path)
    num=get_num_words(text)
    print(num)

def get_num_words(s):
    words =s.split()
    return len(words)

def get_book_text(path):
    with open(path) as f :
        return f.read()


main()

