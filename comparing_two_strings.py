import difflib



a = "ممد"
b = "محمد"
A = difflib.SequenceMatcher(None, a, b,)



print(A.ratio())
