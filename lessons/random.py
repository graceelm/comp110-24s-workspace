pet: dict[str, int] = {"Louie": 8, "Bo": 4}
print(pet)
pet.pop("Bo")
print(pet)
pet["Bear"] = 1
print(pet)
print(len(pet))
pet.pop("Louie")
pet[0] = {"Bella": 8}
print(pet)