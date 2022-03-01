"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150



# Print a dictionary literal representation
print(schools)

# Acces a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students" )

#Remove a key-value pair from a dictionary by its key.

schools.pop("Duke")

# Test for existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

#Update/ Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

# Demonstration of dictionary literals 

# Empty dictionary leteral
schools = {} # same as dict()

# Alternatively initalize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# Example looping over they keys of a dict
for school in schools:
    print(f"Key: {school} - > Value: {schools[school]} ")
