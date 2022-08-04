def main():
    word = input("Enter the reference:\n")
    author = word[0:word.find(")")+1].title().replace(" And " ," and ")
    remain_sent = word[word.find(")")+1 : ]
    title = remain_sent[0 : remain_sent.find(",")]
    Title = title[1:].lower()
    title2 = Title.capitalize()
    x = remain_sent[y.find(","):]
    print("Reformatted reference:\n" +author,title2+x)
    
main()