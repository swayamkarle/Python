a=(input("Enter a String:"))
alpha=0
special=0
digits=0

for i in range(len(a)):
    if (a[i].isalpha()):
        alpha+=1
    elif (a[i].isdigits()):
        digits+=1
    else:
        special=special+1
print("Special Characters in the string are:", special)
print("Alphabets Characters in the string are:", alpha)
print("Digits Characters in the string are:", digits)
