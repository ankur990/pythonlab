Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string=input("Enter the string ")
freq=[None]*len(string)
for i in range(0,len(string)):
freq[i]=1.
for j in range(i+1,len(string)):
if(string[i]==string[j]):
freq[i]=freq[i]+1.
string=string[:j]+'0'+string[j+1:];