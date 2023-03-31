def main():
    path ="/home/nandu/workspace/github.com/nandunagesh123/bookbot/books/frankenstein.txt"
    text=get_book_text(path)
    num=get_num_words(text)
    char_dict = get_char_dict(text)
    get_report(char_dict,path,num)
    


def get_num_words(s):
    words =s.split()
    return len(words)

def get_book_text(path):
    with open(path) as f :
        return f.read()
        
def get_char_dict(text):
    chars={}
    for i in text:
        l= i.lower()
        if l in chars:
            chars[l] +=1
        else:
            chars[l] =1
    return chars

def convert_dict_to_list(char_dict):
    return list(char_dict.items())

def get_report(char_dict,path,num):
    print(f"----Begin Report of {path}--- ")
    print(f"{num} words found in the document")
    print("\n")
    l=convert_dict_to_list(char_dict)
    l.sort()
    for i in l:
        if  i[0].isalpha() == False:
            continue
        print(f"The '{i[0]}' was found {i[1]} times ")


    print("---END Report---")





main()

