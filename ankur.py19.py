def toList(string):
    temp = []
    for x in string:
        temp.append(x)
 def toString(List):
    return ''.join(List)
 def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)] += 1
    return count
