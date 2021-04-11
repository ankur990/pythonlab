def sortLexo(my_string):
    words = my_string.split
    words.sort()
    for i in words:
        print( i ) 
if __name__ == '__main__':
      
    my_string = "hello this is example how to sort " \
              "the word in alphabetical manner"
    sortLexo(my_string)
