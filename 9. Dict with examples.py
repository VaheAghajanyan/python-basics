my_dict = {}

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

value1 = my_dict["key1"]
value2 = my_dict.get("key2")

my_dict["key4"] = "value4"

my_dict["key1"] = "new_value1"

del my_dict["key3"]

if "key2" in my_dict:
    print("Key exists in dictionary.")

for key, value in my_dict.items():
    print(f"{key}: {value}")