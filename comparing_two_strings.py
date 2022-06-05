import difflib



a = "ممد"
b = "محمد"
A = difflib.SequenceMatcher(None, a, b,)



R = A.ratio()
#the higher R is ; the more similar a and b are
print(R)
