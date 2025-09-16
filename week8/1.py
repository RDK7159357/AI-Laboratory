from pyswip import Prolog

# Step 1: FOL translations (hardcoded from your exercise)
fol_statements = {
    "a": "∃x (Boy(x) ∧ Sharp(x) ∧ Intelligent(x))",
    "b": "∃x (Boy(x) ∧ ¬Intelligent(x))",
    "c": "∃x (Student(x) ∧ ClearJEE(x)) ∧ ∀y (Student(y) ∧ ¬ClearJEE(y) → ClearSAT(y))",
    "d1": "∃x (White(x) ∧ ¬Milk(x))",
    "d2": "∀x (Milk(x) → White(x))",
    "e1": "∀x (Day(x) ∧ ¬Sunday(x) → Breakfast_non_sunday(x))",
    "e2": "∀x (Sunday(x) → Breakfast_sunday(x))"
}

# Step 2: Equivalent Prolog facts/rules
prolog_kb = """
boy(john). boy(raj).
sharp(john). intelligent(john).
boy(rahul).  % Rahul is a boy but not intelligent

student(neetha). clearjee(neetha).
student(ravi). clearsat(ravi).

milk(cowmilk). white(cowmilk).
white(chalk).  % Chalk is white but not milk

day(mon). day(tue). day(wed). day(thu). day(fri). day(sat). day(sun).
sunday(sun).

breakfast_non_sunday(D) :- day(D), \\+ sunday(D).
breakfast_sunday(D) :- sunday(D).
"""

# Step 3: Load into Prolog
def setup_prolog():
    prolog = Prolog()
    for stmt in prolog_kb.strip().split("\n"):
        if stmt.strip():
            prolog.assertz(stmt.strip().rstrip("."))
    return prolog

# Step 4: Ask queries
if __name__ == "__main__":
    print("FOL Translations:")
    for k, v in fol_statements.items():
        print(f"{k}: {v}")

    prolog = setup_prolog()
    print("\nSample Queries:")

    print("Who are sharp boys?")
    for sol in prolog.query("boy(X), sharp(X)."):
        print(sol)

    print("\nWho are students that cleared SAT?")
    for sol in prolog.query("student(X), clearsat(X)."):
        print(sol)

    print("\nWhich things are white but not milk?")
    for sol in prolog.query("white(X), \\+ milk(X)."):
        print(sol)

    print("\nOn which days is breakfast served normally?")
    for sol in prolog.query("breakfast_non_sunday(D)."):
        print(sol)

    print("\nOn which day is breakfast served till 9:15?")
    for sol in prolog.query("breakfast_sunday(D)."):
        print(sol)
