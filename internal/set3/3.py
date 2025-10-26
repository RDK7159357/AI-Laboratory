from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies
from sympy.logic.inference import satisfiable
# c. Check the availability
def parse_atom(atom):
    mapping = {"rain": "Rain", "fog": "Fog", "sail": "Sail", "lifesaving": "Life", 
               "trophy": "Trophy", "cs": "CS", "dm": "DM", "neetha": "Neetha", "takes": "Takes"}
    return symbols(mapping.get(atom.strip(), atom.strip()))

def parse_sentence(s):
    s = s.lower().strip()
    if "if" in s and "then" in s:
        cond, result = s.split("then")
        return Implies(parse_atom(cond.replace("if", "").strip()), 
                      parse_atom(result.strip()))
    elif "not" in s:
        return Not(parse_atom(s.replace("not", "").strip()))
    return parse_atom(s)

def check_validity(premises, conclusion):
    combined = And(*[parse_sentence(p) for p in premises])
    result = satisfiable(And(combined, Not(parse_sentence(conclusion))))
    return f"'{conclusion}' is {'FALSE' if result else 'TRUE'}"

premises = [
    "if not rain or not fog then sail and lifesaving",
    "if sail then trophy",
    "not trophy"
]
print(check_validity(premises, "rain"))
