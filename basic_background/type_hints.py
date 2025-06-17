## lesson 1 - type hints

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("daniel", "gregg"))

# key points:
# using type hints (the 'str' bit after the function arguments)
# enables the code editor to provide hints as to what arguments need to be provided for a function
# this reduces burden on user memory and time to check up on arguments

#this fails due to int with str:
def name_with_age(name: str, age: int):
    name_age = name + " is this old: " + age
    return name_age

#this works:
def name_with_age(name: str, age: int):
    name_age = name + " is this old: " + str(age)
    return name_age
# with type hints it is easier to identify this issue. 

# you can also use 'generic' types (e.g. lists, dicts, etc)
def process_items(items: list[str]):
    for item in items:
        print(item.capitalize)
    
def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


