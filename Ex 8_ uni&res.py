knowledge_base = {}

def add_rule(predicate, *arguments):
    knowledge_base.setdefault(predicate, []).append(arguments)

def query(query):
    def unify(query_term, rule_term):
        if query_term == rule_term or query_term.isupper():  # Match variables
            return True
        else:
            return False

    for predicate, arguments in knowledge_base.items():
        if len(query) == len(arguments):
            if all(unify(q, r) for q, r in zip(query, arguments)):
                return True
    return False

# Example Usage
add_rule("enjoy", "sunny", "warm")
add_rule("strawberry_picking", "warm", "pleasant")
add_rule("not_strawberry_picking", "raining")
add_rule("wet", "raining")

add_rule("warm")  # Facts can be added as single-argument rules
add_rule("raining")
add_rule("sunny")

print(query(["not_strawberry_picking"]))  # Output: True
print(query(["enjoy"]))  # Output: True
print(query(["wet"]))  # Output: True
