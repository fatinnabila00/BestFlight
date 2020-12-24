d = 256
f1 = open("stopword.txt","r")
stop = f1.read()
f1.close()
# pat  -> pattern
# txt  -> text
# q    -> A prime number

def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1
    if N < M:
        return 0

    # The value of h would be "pow(d, M-1)%q"
    for i in range(M - 1):
        h = (h * d) % q

        # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

        # Slide the pattern over text one by one
    for i in range(N - M + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i + j] != pat[j]:

                    break

            j += 1
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == M:
                print(pat + " found at index " + str(i))
                remove.append(pat)


        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q

            # Driver program to test the above function
if __name__ == "__main__":

#hongkong1
 print("Stopwords for hongkong1.txt :")
 f = open("hongkong1.txt", "r")
 text1 = f.read()
 f.close()

 remove = []
 newText = []

 mylist = text1.lower().split(None)
 mylist2 = stop.lower().split(None)
 q = 101  # A prime number


 for item in mylist2:
  pat = " "+ item + " "
  search(pat, text1, q)

 remove = list(dict.fromkeys(remove))
 print("\n", len(remove), " stop words found")
 for var in mylist:
  if var == '':
     mylist.remove(var)

 newList=[]
 for i in mylist:
    word = " "+ i + " "
    newList.append(word)

 newText = [ele for ele in newList if ele not in remove]

f = open("newhongkong1.txt", "w")
for item in newText:
 f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")


#hongkong2
print("Stopwords for hongkong2.txt :")
f = open("hongkong2.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newhongkong2.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#hongkong3
print("Stopwords for hongkong3.txt :")
f = open("hongkong3.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newhongkong3.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#hongkong4
print("Stopwords for hongkong4.txt :")
f = open("hongkong4.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newhongkong4.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#hongkong5
print("Stopwords for hongkong5.txt :")
f = open("hongkong5.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newhongkong5.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#taiwan1
print("Stopwords for taiwan1.txt :")
f = open("taiwan1.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtaiwan1.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#taiwan2
print("Stopwords for taiwan2.txt :")
f = open("taiwan2.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtaiwan2.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#taiwan3
print("Stopwords for taiwan3.txt :")
f = open("taiwan3.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtaiwan3.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#taiwan4
print("Stopwords for taiwan4.txt :")
f = open("taiwan4.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtaiwan4.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#taiwan5
print("Stopwords for taiwan5.txt :")
f = open("taiwan5.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtaiwan5.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#van1
print("Stopwords for van1.txt :")
f = open("van1.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newvan1.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#van2
print("Stopwords for van2.txt :")
f = open("van2.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newvan2.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#van3
print("Stopwords for van3.txt :")
f = open("van3.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newvan3.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#van4
print("Stopwords for van4.txt :")
f = open("van4.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newvan4.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#van5
print("Stopwords for van5.txt :")
f = open("van5.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newvan4.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#van5
print("Stopwords for van5.txt :")
f = open("van5.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newvan5.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#LAv1
print("Stopwords for LAv1.txt :")
f = open("LAv1.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newLAv1.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#LAv2
print("Stopwords for LAv2.txt :")
f = open("LAv2.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newLAv2.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#LAv3
print("Stopwords for LAv3.txt :")
f = open("LAv3.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newLAv3.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#LAv4
print("Stopwords for LAv4.txt :")
f = open("LAv4.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newLAv4.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#LAv5
print("Stopwords for LAv5.txt :")
f = open("LAv5.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newLAv5.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#Bostonv1
print("Stopwords for Bostonv1.txt :")
f = open("Bostonv1.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newBostonv1.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#Bostonv2
print("Stopwords for Bostonv2.txt :")
f = open("Bostonv2.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newBostonv2.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#Bostonv3
print("Stopwords for Bostonv3.txt :")
f = open("Bostonv3.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newBostonv3.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#Bostonv4
print("Stopwords for Bostonv4.txt :")
f = open("Bostonv4.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newBostonv4.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#Bostonv5
print("Stopwords for Bostonv5.txt :")
f = open("Bostonv5.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newBostonv5.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#Dohav1
print("Stopwords for Dohav1.txt :")
f = open("Dohav1.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newDohav1.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#Dohav2
print("Stopwords for Dohav2.txt :")
f = open("Dohav2.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newDohav2.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#Dohav3
print("Stopwords for Dohav3.txt :")
f = open("Dohav3.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newDohav3.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#Dohav4
print("Stopwords for Dohav4.txt :")
f = open("Dohav4.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newDohav4.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#Dohav5
print("Stopwords for Dohav5.txt :")
f = open("Dohav5.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newDohav5.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#chicago1
print("Stopwords for chicago1.txt :")
f = open("chicago1.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newchicago1.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#chicago2
print("Stopwords for chicago2.txt :")
f = open("chicago2.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newchicago2.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#chicago3
print("Stopwords for chicago3.txt :")
f = open("chicago3.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newchicago3.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#chicago4
print("Stopwords for chicago4.txt :")
f = open("chicago4.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newchicago4.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")



#chicago5
print("Stopwords for chicago5.txt :")
f = open("chicago5.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newchicago5.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#texas1
print("Stopwords for texas1.txt :")
f = open("texas1.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtexas1.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#texas2
print("Stopwords for texas2.txt :")
f = open("texas2.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtexas2.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#texas3
print("Stopwords for texas3.txt :")
f = open("texas3.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtexas3.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#texas4
print("Stopwords for texas4.txt :")
f = open("texas4.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtexas4.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#texas5
print("Stopwords for texas5.txt :")
f = open("texas5.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtexas5.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#tokyo1
print("Stopwords for tokyo1.txt :")
f = open("tokyo.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtokyo1.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")



#tokyo2
print("Stopwords for tokyo2.txt :")
f = open("tokyo2.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtokyo2.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")


#tokyo3
print("Stopwords for tokyo3.txt :")
f = open("tokyo3.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtokyo3.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#tokyo4
print("Stopwords for tokyo4.txt :")
f = open("tokyo4.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtokyo4.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")

#tokyo5
print("Stopwords for tokyo5.txt :")
f = open("tokyo5.txt", "r")
text1 = f.read()
f.close()

remove = []
newText = []

mylist = text1.lower().split(None)
mylist2 = stop.lower().split(None)
q = 101  # A prime number

for item in mylist2:
    pat = " " + item + " "
    search(pat, text1, q)

remove = list(dict.fromkeys(remove))
print("\n", len(remove), " stop words found")

for var in mylist:
    if var == '':
        mylist.remove(var)

newList = []
for i in mylist:
    word = " " + i + " "
    newList.append(word)

newText = [ele for ele in newList if ele not in remove]

f = open("newtokyo5.txt", "w")
for item in newText:
    f.write(item)
f.close
print("\n Stop words succesfully removed, new text file generated.")
print("---------------------------------------------------------------\n ")