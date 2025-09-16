from pyswip import Prolog

def translate(sentence):
    s = sentence.lower()

    if "not all" in s and "car" in s:
        return "∃x [Car(x) ∧ ¬HasCarb(x)]", "car(tata). car(bmw)."
    elif "some people" in s and ("religious" in s or "pious" in s):
        return "∃x [Person(x) ∧ (Religious(x) ∨ Pious(x))]", "person(john). religious(john). person(raj). pious(raj)."
    elif "no dogs" in s and "intelligent" in s:
        return "∀x [Dog(x) → ¬Intelligent(x)]", "dog(browny). dog(tommy)."
    elif "all babies" in s and "illogical" in s:
        return "∀x [Baby(x) → Illogical(x)]", "baby(ram). illogical(ram)."
    elif "every number" in s and ("negative" in s or "square root" in s):
        return "∀x [Number(x) → (Negative(x) ∨ HasSquareRoot(x))]", "number(1). number(-2). negative(-2). hasSquareRoot(1)."
    elif "some numbers" in s and "not real" in s:
        return "∃x [Number(x) ∧ ¬Real(x)]", "number(i). notreal(i)."
    elif "every connected" in s and "graph" in s:
        return "∀g [(Graph(g) ∧ Connected(g) ∧ CircuitFree(g)) → Tree(g)]", "graph(g1). connected(g1). circuitfree(g1)."
    else:
        return "Translation not available.", ""

def main():
    prolog = Prolog()
    print("Enter English sentences (type 'exit' to quit):")
    
    while True:
        sentence = input("Sentence: ")
        if sentence.lower() == "exit":
            break

        fol, kb = translate(sentence)
        print("FOL:", fol)
        
        if kb:
            # Load into Prolog
            for fact in kb.split("."):
                if fact.strip():
                    prolog.assertz(fact.strip())
            
            # Example queries
            print("\nSample Queries:")
            if "car" in kb:
                for sol in prolog.query("car(X)."):
                    print("Car:", sol["X"])
            if "person" in kb:
                for sol in prolog.query("person(X)."):
                    print("Person:", sol["X"])
            if "dog" in kb:
                for sol in prolog.query("dog(X)."):
                    print("Dog:", sol["X"])
            if "baby" in kb:
                for sol in prolog.query("baby(X)."):
                    print("Baby:", sol["X"])
            if "number" in kb:
                for sol in prolog.query("number(X)."):
                    print("Number:", sol["X"])
            if "graph" in kb:
                for sol in prolog.query("graph(X)."):
                    print("Graph:", sol["X"])
        print("\n" + "-"*40 + "\n")

if __name__ == "__main__":
    main()
