from selectolax.parser import Node, HTMLParser
from typing import Union

def parse_raw_attributes(node: Union[Node, str], selectors:list[dict]) -> dict:
    
    if not issubclass(Node, type(node)):
        node = HTMLParser(node)
    
    parsed = {}
    
    for select in selectors:
        name = select.get("name")
        match = select.get("match")
        type_ = select.get("type")
        selector = select.get("selector")
        
        if match == "all":
            matched = node.css(selector)
            
            if type_ == "node":
                parsed[name] = matched
                
            elif type_ == "text":
                parsed[name] = [m.text() for m in matched]
            
        if match == "first":
            matched = node.css_first(selector)
            
            if type_ == "node":
                parsed[name] = matched
                
            elif type_ == "text":
                parsed[name] = matched.text()
        
    return parsed