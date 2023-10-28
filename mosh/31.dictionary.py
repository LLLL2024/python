customer = {
          "name": "John",
          "age": 30,
          "is_verified": True
}
print(customer.get("birthdate", "Jan, 23, 1990"))

phone = input("phone:")
digits_mapping = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + ""
print(output)
