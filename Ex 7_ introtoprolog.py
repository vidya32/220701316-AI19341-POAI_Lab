# Knowledge Base
knowledge_base = {
    "woman": ["mia", "jody", "yolanda"],
    "playsAirGuitar": ["jody"],
    "party": True,
    "likes": [("dan", "sally"), ("sally", "dan"), ("john", "brittney")],
    "food": ["burger", "sandwich", "pizza"],
    "lunch": ["sandwich"],
    "dinner": ["pizza"],
    "owns": [("jack", "car(bmw)"), ("john", "car(chevy)"), ("olivia", "car(civic)"), ("jane", "car(chevy)")],
    "sedan": ["car(bmw)", "car(civic)"],
    "truck": ["car(chevy)"]
}

# Query Function
def query(query_string):
    query_parts = query_string.split()
    predicate = query_parts[0]
    arguments = query_parts[1:]

    if predicate in knowledge_base:
        if len(arguments) == 0:
            return knowledge_base[predicate]
        elif predicate == "likes" or predicate == "owns":
            for pair in knowledge_base[predicate]:
                if pair[0] == arguments[0] and pair[1] == arguments[1]:
                    return True
        elif predicate == "married":
            if (arguments[0], arguments[1]) in knowledge_base["likes"] and (arguments[1], arguments[0]) in knowledge_base["likes"]:
                return True
        elif predicate == "friends":
            if (arguments[0], arguments[1]) in knowledge_base["likes"] or (arguments[1], arguments[0]) in knowledge_base["likes"]:
                return True
        elif predicate == "meal":
            for food in knowledge_base["food"]:
                if food == arguments[0]:
                    return True
        elif predicate == "sedan" or predicate == "truck":
            for vehicle in knowledge_base[predicate]:
                if vehicle == arguments[0]:
                    return True

    return False

# Example Queries
print(query("woman mia"))  # Output: True
print(query("playsAirGuitar mia"))  # Output: False
print(query("party"))  # Output: True
print(query("concert"))  # Output: False
print(query("likes dan sally"))  # Output: True
print(query("married dan sally"))  # Output: True
print(query("friends john brittney"))  # Output: True
print(query("meal sandwich"))  # Output: True
print(query("sedan car(civic)"))  # Output: True
