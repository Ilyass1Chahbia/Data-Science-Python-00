from typing import Any

def all_thing_is_obj(object: Any) -> int:
    res = type(object)
    if (res == list):
        print(f"List : {res}")
    elif (res == str):
        print(f"{object} is in the kitchen : {res}")
    elif (res == dict):
        print(f"Dict : {res}")
    elif (res == tuple):
        print(f"Tuple : {res}")
    elif (res == set):
        print(f"Set : {res}")
    else:
        print("Type not found")
    return 42
