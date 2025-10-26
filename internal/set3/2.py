# b. Knowledge Representation using FOL – Translate
def translate_math(s):
    s = s.lower()
    if "for each integer x" in s and "x + y = 0" in s:
        return "∀x∈Z ∃y∈Z (x+y=0)"
    elif "there exist an integer x" in s and "x + y = y" in s:
        return "∃x∈Z ∀y∈Z (x+y=y)"
    elif "for all integers x and y" in s and "x.y" in s and "y.x" in s:
        return "∀x∈Z ∀y∈Z (x·y=y·x)"
    elif "there are integers x and y" in s and "x+y=5" in s:
        return "∃x∈Z ∃y∈Z (x+y=5)"
    return "No translation"

while True:
    s = input("Sentence (exit to quit): ")
    if s.lower() == "exit":
        break
    print(f"FOL: {translate_math(s)}\n")
