"""Practicing with dictionaries"""

#Setting up a dictionary
favorite_places: dict[str,str] = {"Mary": "Wilson" , "Lily" : "Quad" , "Pakiza": "Davis"}
print(favorite_places)

#Adding a value to a dictionary
favorite_places["Morgan"] = "room"
favorite_places["Annie"] = "archaeology class"
print(favorite_places)

#Changing key values
favorite_places["Pakiza"] = "bed"
print(favorite_places)

#Deleting from a list
favorite_places.pop("Pakiza")
favorite_places.pop("Lily")
print(favorite_places)
