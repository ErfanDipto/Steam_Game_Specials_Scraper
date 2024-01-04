from selectolax.parser import Node
from datetime import datetime
import re
import pandas as pd


def get_attrs_from_node(node: Node, attr: str):
    
    if node is None or not issubclass(Node, type(node)):
        raise ValueError("The function expects a selectolax node to be provided")
    
    return node.attributes.get(attr)


def get_first_n(tag_list: list, n: int=5):
    
    if tag_list is None or not issubclass(list, type(tag_list)):
        raise ValueError("The function expects a list to be provided")
    
    return tag_list[:n]


def change_date_time(date_time: str, from_fmt: str="%b %d, %Y", to_fmt: str="%d/%m/%Y"):
    dt = datetime.strptime(date_time, from_fmt)
    
    dt = dt.strftime(to_fmt)
    
    return dt


def parsing_currency(s: str):
    
    s = s.split(" ")
    
    return s

def regex(input_string: str, pattern: str, do_what: str="find_all"):
    if do_what == "find_all":
        output_string = re.findall(pattern=pattern, string=input_string)
        return output_string
    elif do_what == "split":
        output_string = re.split(pattern=pattern, string=input_string)
        return output_string
    else:
        raise ValueError("The function expects \"find_all\" or \"split\" to be provided")


def format_and_transform(attrs: dict):
    
    transform = {
        "Thumbnail": lambda n: get_attrs_from_node(n, "src"),
        "Tags": lambda tag_list: get_first_n(tag_list, 5),
        "Release Date": lambda date_: change_date_time(date_, from_fmt="%b %d, %Y", to_fmt="%d/%m/%Y"),
        "Number of Reviewers": lambda reviews: int("".join(regex(input_string=reviews, pattern="[0-9]", do_what="find_all"))),
        "Price Currency": lambda currency_str: regex(input_string=currency_str, pattern=" ", do_what="split")[0],
        "Original Price": lambda price: float("".join(regex(input_string=price, pattern="[0-9.]", do_what="find_all"))),
        "Sale Price": lambda price: float("".join(regex(input_string=price,pattern="[0-9.]", do_what="find_all"))),
        "Discount Percentage": lambda discount: int("".join(regex(input_string=discount, pattern="[0-9.]", do_what="find_all")))
    }
    
    for key, value in transform.items():
        if key in attrs:
            attrs[key] = value(attrs[key])
            
    attrs["Discount Percentage (Calculated)"] = round((((attrs["Original Price"] - attrs["Sale Price"]) / attrs["Original Price"]) * 100), 3)
            
    return attrs

def save_to_file(filename: str="extract", data: list[dict]=None):
    
    if data == None:
        raise ValueError("The function expects data to be provided as list of dictionaries")
    
    df =pd.DataFrame(data=data)
    filename = f"{datetime.now().strftime("%d_%m_%Y_%H_%M")}_{filename}.csv"
    df.to_csv(filename, index=False)
