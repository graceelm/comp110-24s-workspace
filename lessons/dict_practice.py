"""Practicing with dictionaries."""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3 
print(ice_cream)
print("after removing mint: ")
ice_cream.pop("mint")
print(ice_cream)
print("after changing num of orders")
ice_cream["vanilla"] = 10
print(ice_cream)