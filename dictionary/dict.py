# ✅ Creating a dictionary
Me = {
    "key": "value",
    "name": "debalina",
    "age": 19,
    "issingle": True,
    # "mark": 85.3,  # duplicate key example
    "mark": 52.7,  # ✅ the last occurrence will be taken (85.3 ignored)
    "hobbies": ["photography", "sketching", "designing"],  # list as value
    "lang": {       # nested dictionary
        "native": "beng",
        "knows": "hindi",
        "learned": "eng"
    }
}

# ✅ Checking type
print(type(Me))  # <class 'dict'>

# ✅ Printing the dictionary
print(Me)

# ✅ Accessing values using keys
print(Me["name"])     # debalina
print(Me["key"])      # value
print(Me["age"])      # 19
print(Me["mark"])     # 52.7
print(Me["issingle"]) # True

# 📝 Dictionary:
# - Stores data in key:value pairs
# - Keys must be unique (if duplicate → last value taken)
# - Dictionary is unordered, mutable, does not allow duplicate keys

# ✅ Changing value (mutable)
Me["name"] = "DR"
print(Me)  # name changed from 'debalina' → 'DR'

# ✅ Adding new key:value pair
Me["surname"] = "roy"
print(Me)

# ✅ Dictionary built-in methods
print(Me.keys())    # all keys
print(Me.values())  # all values
print(Me.items())   # all key-value pairs (as tuples)
print(Me.get("surname"))  # returns 'roy'

# ✅ update() → updates dictionary with new key-value pairs
# if key already exists → value gets updated
# if key doesn’t exist → new key-value pair is added
Me.update({"age": 20, "city": "Kolkata"})
print(Me)
# here: 'age' updated to 20, new key 'city' added with value 'Kolkata'


#📝 Short Notes (Dictionary)

# Definition: Collection of key:value pairs → {key: value}.
# Properties: Unordered, mutable, keys must be unique.
# Access: dict["key"] or dict.get("key").
# Modify: Add/Update using dict["key"] = value.
# Important methods: .keys(), .values(), .items(), .get(), .update().
