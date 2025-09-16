def translate(sentence):
    s = sentence.lower()

    if "not all" in s and "car" in s:
        return "∃x [Car(x) ∧ ¬HasCarb(x)]"
    elif "some people" in s and ("religious" in s or "pious" in s):
        return "∃x [Person(x) ∧ (Religious(x) ∨ Pious(x))]"
    elif "no dogs" in s and "intelligent" in s:
        return "∀x [Dog(x) → ¬Intelligent(x)]"
    elif "all babies" in s and "illogical" in s:
        return "∀x [Baby(x) → Illogical(x)]"
    elif "every number" in s and ("negative" in s or "square root" in s):
        return "∀x [Number(x) → (Negative(x) ∨ HasSquareRoot(x))]"
    elif "some numbers" in s and "not real" in s:
        return "∃x [Number(x) ∧ ¬Real(x)]"
    elif "every connected" in s and "graph" in s:
        return "∀g [(Graph(g) ∧ Connected(g) ∧ CircuitFree(g)) → Tree(g)]"
    else:
        return "Translation not available."

def main():
    print("Enter English sentences (type 'exit' to quit):")
    while True:
        sentence = input("Sentence: ")
        if sentence.lower() == "exit":
            break
        print("FOL:", translate(sentence), "\n")

if __name__ == "__main__":
    main()
