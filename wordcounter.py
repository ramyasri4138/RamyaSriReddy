def wordcounter(sentence):
    sentencelower=sentence.lower().split()
    wordcount={}
    for word in sentencelower:
        if word in wordcount:
            wordcount[word]+=1
        else:
            wordcount[word]=1
    return wordcount
def main():
    sentence=input("enter a sentence: ")
    wordscounted=wordcounter(sentence)
    for word,count in wordscounted.items( ):
        print(f"{word}:{count}")
main()