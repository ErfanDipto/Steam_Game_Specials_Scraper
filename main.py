# from playwright.sync_api import sync_playwright
from utils import extract
from utils.parse import parse_raw_attributes
from utils.process import format_and_transform
from utils.process import save_to_file
from config.tools import get_config
from selectolax.parser import HTMLParser

# URL = "https://store.steampowered.com/specials"

if __name__ == "__main__":
    
    config = get_config(load_from_file=False)
    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=True)
    #     page = browser.new_page()
    #     page.goto(URL)
        
    #     page.wait_for_load_state("networkidle")
    #     page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
    #     page.wait_for_load_state("domcontentloaded")
    #     page.wait_for_selector("div[class*=StoreSaleWidgetRelease]")
        
        # page.screenshot(path="./steam.png", full_page=True)
    # html = page.inner_html("body")
    html = extract.extract_full_body_html(
        # from_url=URL,
        from_url=config.get("url"),
        # wait_for="div[class*=StoreSaleWidgetContainer]"
        wait_for=config.get("container").get("selector")
        )
    
    # tree = HTMLParser(html)
    
    # divs = tree.css("div[class*=StoreSaleWidgetContainer]")
    # print(len(divs))
    
    
    nodes = parse_raw_attributes(html, [config.get("container")])
    
    game_data = []
    
    for node in nodes.get("store_sale_divs"):
    # for d in divs:
        attrs = parse_raw_attributes(node, config.get("item"))
        # attrs = parse_raw_attributes(d, config.get("item"))
        attrs = format_and_transform(attrs)
        game_data.append(attrs)
        # print(node, nodes.get("store_sale_divs"))
        
        # title -> no change
        # Thumbnail -> node to image src attribute
        # tags -> first 5
        # release date -> change date format
        # review -> no change
        # currency -> first split of original price
        
        # number of reviewers -> only numbers
        # original price -> only number
        # sale price -> only number
        # discount -> no change
        
        
        # {'Title': 'EA SPORTS FC™ 24', 
        # 'Umage URL': <Node img>, 
        # 'Tags': ['Sports', 'Football (Soccer)', 'Controller', 'PvP', 'Competitive', 'eSports', 'PvE', 'Multiplayer', '3D', 'First-Person', 'Simulation', 'Realistic', 'Action', 'Local Multiplayer', 'Co-op', 'Local Co-Op', 'Family Friendly', 'Online Co-Op', 'Singleplayer', 'Early Access'], 
        # 'Release Date': 'Sep 29, 2023', 
        # 'Reiew': 'Mixed', 
        # 'Number of Reviewers': '| 21,167 
        # 'Original Price': 'A$ 99.95', 
        # 'Sale Price': 'A$ 49.97', 
        # 'Discount': '-50%'}
        
        
        # title = d.css_first("div[class*=StoreSaleWidgetTitle]").text()
        
        # img_url = d.css_first("img[class*=CapsuleImage]").attributes.get("src")
        
        # tags_ = d.css("div[class*=StoreSaleWidgetTags] > a")
        
        # tags = [tag.text() for tag in tags_[:5]]
        
        # release_date = d.css_first("div[class*=WidgetReleaseDateAndPlatformCtn] > div[class*=StoreSaleWidgetRelease]").text()
        
        # review = d.css_first("div[class*=ReviewScoreValue] > div").text()
        
        # num_reviewers = d.css_first("div[class*=ReviewScoreValue] > div[class*=ReviewScoreCount]").text()
        
        # original_price = d.css_first("div[class*=StoreOriginalPrice]").text()
        
        # sale_price = d.css_first("div[class*=StoreSalePriceBox]").text()
        
        # discount = d.css_first("div[class*=StoreSaleDiscountBox]").text()
        
        
        # attrs = {
        #     "Title": title,
        #     "Thumbnail": img_url,
        #     "Tags": tags,
        #     "Release Date": release_date,
        #     "Review": review,
        #     "Number of Reviewers": num_reviewers,
        #     "Original Price": original_price,
        #     "Sale Price": sale_price,
        #     "Discount (%)": discount
        # }
        
    save_to_file(filename="game_data_extract", data=game_data)
            