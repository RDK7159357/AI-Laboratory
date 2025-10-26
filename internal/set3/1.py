from pyswip import Prolog
# Exercises on Knowledge Representation using FOL
# a. Knowledge Representation using FOL – Translate
def translate(s):
    s = s.lower()
    if "not all" in s and "car" in s:
        return "∃x[Car(x)∧¬HasCarb(x)]", "car(tata). car(bmw)."
    elif "some people" in s and ("religious" in s or "pious" in s):
        return "∃x[Person(x)∧(Religious(x)∨Pious(x))]", "person(john). religious(john)."
    elif "no dogs" in s and "intelligent" in s:
        return "∀x[Dog(x)→¬Intelligent(x)]", "dog(browny)."
    elif "all babies" in s and "illogical" in s:
        return "∀x[Baby(x)→Illogical(x)]", "baby(ram). illogical(ram)."
    elif "every number" in s:
        return "∀x[Number(x)→(Negative(x)∨HasSquareRoot(x))]", "number(1). number(-2)."
    elif "every connected" in s and "graph" in s:
        return "∀g[(Graph(g)∧Connected(g)∧CircuitFree(g))→Tree(g)]", "graph(g1). connected(g1)."
    return "No translation", ""

prolog = Prolog()
while True:
    s = input("Sentence (exit to quit): ")
    if s.lower() == "exit":
        break
    fol, kb = translate(s)
    print(f"FOL: {fol}")
    if kb:
        for fact in kb.split("."):
            if fact.strip():
                prolog.assertz(fact.strip())
    print()
