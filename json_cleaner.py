import pandas as pd
import json
sample_json = [
    {
        "MainId": 1111,
        "firstName": "Sherlock",
        "lastName": "Homes",
        "categories": [
            {
                "CategoryID": 1,
                "categories": [
                    {"category 1": "root beer",
                     "category 2": "ham",
                     "category 3": "soda"}]
            }
        ]
    },
    {
        "MainId": 122,
        "firstName": "James",
        "lastName": "Watson",
        "categories": [
            {
                "CategoryID": 2,
                "firstName": "2nd_lvl_first_name",
                "categories": [{"category 2": "apple pie",
                                "category 3": "jerkey",
                                "category 4": "orange ice cream"}]
            }
        ]
    },
    {
        "MainId": 133,
        "firstName": "John",
        "lastName": "Watson",
        "categories": [
            {"category 2": "apple pie",
             "firstName": "3rd_lvl_first_name",
             "category 3": "ham",
             "category 4": "blue ice cream"}
        ]
    },
    {
        "MainId": 144,
        "firstName": "Jackob",
        "lastName": "Watson"
    }
]


def check_list_keys(data):
    '''returns a list of keys that resolve to list data type for data'''
    return [key for key in data if data.get(key) \
                and isinstance(data[key], list)]

def recursive_search(data, search_keys):

    if isinstance(data, dict):
        
        list_keys = check_list_keys(data)
        search_data = {k: data[k] for k in data if k not in list_keys and k in search_keys}
    # scenario 1: data is a dict and no keys resolve to a list (base case) 
        if not list_keys:
        
            return search_data
        
    # scenario 2: data is a dict, but one or more keys resolve to a list
        
        else:
           
            for key in list_keys:
                search_data[key] = recursive_search(data[key], search_keys)
            return search_data 
    
    # scenario 3: data is a list and we need to iterate through the list
    elif isinstance(data, list):
        return [recursive_search(item, search_keys) for item in data]


search_keys = ["MainId", "lastName", "firstName"]
results = recursive_search(sample_json, search_keys = search_keys )
   
