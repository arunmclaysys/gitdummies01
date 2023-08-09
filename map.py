def main():
    #yell(["Hello", "to", "CS50"])
    yell("this", "is", "CS50")

#Basic way
'''def yell(words):
    upper_words = []
    for word in words:
        upper_words.append(word.upper())
    print(*upper_words)'''


#Pretty decent way to write code. as we have used * here for unpacking
'''def yell(*words, end=""):
     for word in words:
         print(word.upper())'''

#using map
'''def yell(*words, end=""):
     uppercased = map(str.upper, words)
     print(*uppercased)'''

#using list comprehension
def yell(*words, end=""):
     uppercased = [word.upper() for word in words]
     print(*uppercased)

if __name__ == "__main__":
    main()