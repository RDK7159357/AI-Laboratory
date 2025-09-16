from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies
from sympy.logic.inference import satisfiable

# Simple parser for natural language → FOL
def parse_sentence(sentence):
    sentence = sentence.lower().strip()

    Rain, Fog, Sail, Life, Trophy, CS, DM, Neetha, Takes = \
        symbols("Rain Fog Sail Life Trophy CS DM Neetha Takes")

    if "if" in sentence and "then" in sentence:
        cond, result = sentence.split("then")
        cond = cond.replace("if", "").strip()
        return Implies(parse_atom(cond), parse_atom(result.strip()))
    elif "not" in sentence:
        return Not(parse_atom(sentence.replace("not", "").strip()))
    else:
        return parse_atom(sentence)

def parse_atom(atom):
    Rain, Fog, Sail, Life, Trophy, CS, DM, Neetha, Takes = \
        symbols("Rain Fog Sail Life Trophy CS DM Neetha Takes")
    mapping = {
        "rain": Rain, "fog": Fog, "sail": Sail, "lifesaving": Life,
        "trophy": Trophy, "cs": CS, "dm": DM, "neetha": Neetha, "takes": Takes
    }
    return mapping.get(atom.strip(), symbols(atom.strip()))

def check_validity(premises, conclusion):
    formulas = [parse_sentence(p) for p in premises]
    conclusion_formula = parse_sentence(conclusion)

    combined = And(*formulas)
    result = satisfiable(And(combined, Not(conclusion_formula)))

    if result:
        return f"Conclusion '{conclusion}' is FALSE (counterexample: {result})"
    else:
        return f"Conclusion '{conclusion}' is TRUE (logically valid)"

# Example run
premises = [
    "if not rain or not fog then sail and lifesaving",
    "if sail then trophy",
    "not trophy"
]
conclusion = "rain"

print(check_validity(premises, conclusion))
