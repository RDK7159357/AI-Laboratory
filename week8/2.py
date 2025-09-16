def is_proposition(statement):
    stmt = statement.lower().strip()

    # Rule 1: If it contains a variable (like x, y) without quantifier, it's not a proposition
    if "x" in stmt and ("=" in stmt or "∈" in stmt):
        return False, "Not a proposition because it contains a free variable (x)."

    # Rule 2: If it is a declarative sentence (like 'I shall sleep or study'), it's a proposition
    if stmt.endswith(".") or "or" in stmt or "and" in stmt:
        return True, "It is a proposition because it is a declarative statement with a definite truth value."

    # Default case: Assume not a proposition
    return False, "Not a proposition because it does not express a definite truth value."


def main():
    inputs = [
        "I shall sleep or study.",
        "x^2 + 5x + 6 = 0 such that x ∈ integers."
    ]

    print("Input Sentences and their Status:\n")
    for s in inputs:
        status, reason = is_proposition(s)
        print(f"Sentence: {s}")
        print(f"Proposition: {status}")
        print(f"Reason: {reason}\n")


if __name__ == "__main__":
    main()
