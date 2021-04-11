   st = st.split(" ")
   for i in range(0, len(st)):
      st[i] = "".join(st[i])
      dupli = Counter(st)
      s = " ".join(dupli.keys())
      print ("After removing the sentence is ::>",s)
   if __name__ == "__main__":
      st = input("Enter the sentence")
remov_duplicates(st)
