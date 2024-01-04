import json

_config = {
    
    "url": "https://store.steampowered.com/specials",
    
    "meta": {
        "name": "Steam Sale Scraper",
        "Description": "Extracts descriptions of the highest discounted games on Steam",
        "Author": "Erfanul Haque",
        "Verson": 0.1
    },
    
    "container": {
        "name": "store_sale_divs",
        "selector": "div[class*=StoreSaleWidgetContainer]",
        "match": "all",
        "type": "node"
        },
    
    "item": [
        
        {
            "name": "Title",
            "selector": "div[class*=StoreSaleWidgetTitle]",
            "match": "first",
            "type": "text"
        },
        
        {
            "name": "Thumbnail",
            "selector": "img[class*=CapsuleImage]",
            "match": "first",
            "type": "node"
        },
        
        {
            "name": "Tags",
            "selector": "div[class*=StoreSaleWidgetTags] > a",
            "match": "all",
            "type": "text"
        },
        
        {
            "name": "Release Date",
            "selector": "div[class*=WidgetReleaseDateAndPlatformCtn] > div[class*=StoreSaleWidgetRelease]",
            "match": "first",
            "type": "text"
        },
        
        {
            "name": "Reiew",
            "selector": "div[class*=ReviewScoreValue] > div",
            "match": "first",
            "type": "text"
        },
        
        {
            "name": "Number of Reviewers",
            "selector": "div[class*=ReviewScoreValue] > div[class*=ReviewScoreCount]",
            "match": "first",
            "type": "text"
        },
        
        {
            "name": "Price Currency",
            "selector": "div[class*=StoreOriginalPrice]",
            "match": "first",
            "type": "text"
        },
        
        {
            "name": "Original Price",
            "selector": "div[class*=StoreOriginalPrice]",
            "match": "first",
            "type": "text"
        },
        
        {
            "name": "Sale Price",
            "selector": "div[class*=StoreSalePriceBox]",
            "match": "first",
            "type": "text"
        },
        
        {
            "name": "Discount Percentage",
            "selector": "div[class*=StoreSaleDiscountBox]",
            "match": "first",
            "type": "text"
        }
        

        
    ]
    
}

def get_config(load_from_file=False):
    
    if load_from_file:
        with open("config.json", "r") as f:          
            return json.load(f)
    
    return _config

def generate_config():
    with open("config.json", "w") as f:
        json.dump(_config, f, indent=4)
        
if __name__ == "__main__":
    generate_config()
    # get_config(load_from_file=False)