#  Install the Python Requests library:
# `pip install requests`
# 8FFCR4E3QJ6DFLMO4D55MCWHLTJK5LMC1BHAZ2AIKD7MD4NSD1BLBLDKQY3QWO4DN6NR2Q29EV6IYOCQ
# https://www.nike.com/nl/en/t/air-force-1-07-shoes-GjGXSP/CW2288-111
from scrapingbee import ScrapingBeeClient

file = open('demofile2.txt', 'wt')

client = ScrapingBeeClient(
    api_key='8FFCR4E3QJ6DFLMO4D55MCWHLTJK5LMC1BHAZ2AIKD7MD4NSD1BLBLDKQY3QWO4DN6NR2Q29EV6IYOCQ')


extract_rules = {
    "images": {
        "selector": "img",
        "type": "list",
                "output": {
                    "src": "img@src",
                    "alt": "img@alt",
                }
    }
}

js_scenario = {
    "instructions": [
        {"infinite_scroll":  # Scroll the page until the end
         {
             "max_count": 0,  # Maximum number of scroll, 0 for infinite
             "delay": 2000  # Delay between each scroll, in ms

         }
        }
    ]
}

response = client.get(
    'https://www.nike.com/nl/en/t/air-force-1-07-shoes-GjGXSP/CW2288-111',
    params={
        "extract_rules":  extract_rules,
        "js_scenario": js_scenario
        
    },
)
file.write(response.content.decode(
    "utf-8").encode('cp850', 'replace').decode('cp850'))


file.close()
# output = str(response.content, 'UTF-8')
