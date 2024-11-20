family_tree = {
    "peter": ["chris", "helen"],
    "betty": ["chris", "helen"],
    "john": ["jeny"],
    "helen": ["jeny", "kevin", "lisa"],
    "chris": ["kevin", "lisa"],
    "kevin": [],  # Assuming Kevin doesn't have children
    "jeny": [],
    "lisa": [],
}

gender = {
    "peter": "male",
    "john": "male",
    "chris": "male",
    "kevin": "male",
    "betty": "female",
    "jeny": "female",
    "lisa": "female",
    "helen": "female"
}

def is_male(person):
    return gender[person] == "male"

def is_female(person):
    return gender[person] == "female"

def is_parent(parent, child):
    return child in family_tree.get(parent, [])

def is_child(child, parent):
    return parent in family_tree[child]

def is_sibling(person1, person2):
    return set(family_tree[person1]) & set(family_tree[person2])

# Example queries
print(is_male("john"))  # Output: True
print(is_female("lisa"))  # Output: True
print(is_parent("kevin", "chris"))  # Output: False (since Kevin has no children)
print(is_child("betty", "helen"))  # Output: True
print(is_sibling("peter", "betty"))  # Output: True
