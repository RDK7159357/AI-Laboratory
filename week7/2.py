def translate_math(sentence):
    s = sentence.lower()

    if "for each integer x" in s and "x + y = 0" in s:
        return "∀x ∈ Z ∃y ∈ Z (x + y = 0)"
    elif "there exist an integer x" in s and "x + y = y" in s:
        return "∃x ∈ Z ∀y ∈ Z (x + y = y)"
    elif "for all integers x and y" in s and ("x.y" in s or "x * y" in s) and "y.x" in s:
        return "∀x ∈ Z ∀y ∈ Z (x · y = y · x)"
    elif "there are integers x and y" in s and "x+y=5" in s:
        return "∃x ∈ Z ∃y ∈ Z (x + y = 5)"
    else:
        return "No translation available."

def main():
    print("Enter mathematical sentences (type 'exit' to quit):\n")
    while True:
        sentence = input("Sentence: ")
        if sentence.lower() == "exit":
            break
        print("FOL:", translate_math(sentence), "\n")

if __name__ == "__main__":
    main()
