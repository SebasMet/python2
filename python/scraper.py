#  Install the Python Requests library:
# `pip install requests`
# 8FFCR4E3QJ6DFLMO4D55MCWHLTJK5LMC1BHAZ2AIKD7MD4NSD1BLBLDKQY3QWO4DN6NR2Q29EV6IYOCQ
# https://www.nike.com/nl/en/t/air-force-1-07-shoes-GjGXSP/CW2288-111
from scrapingbee import ScrapingBeeClient
import hdfs

client1 = hdfs.InsecureClient('http://localhost:9870/')

client = ScrapingBeeClient(
    api_key='8FFCR4E3QJ6DFLMO4D55MCWHLTJK5LMC1BHAZ2AIKD7MD4NSD1BLBLDKQY3QWO4DN6NR2Q29EV6IYOCQ')

file = open('demofile2.txt', 'wt')
for num in range(0, 100, 10):
    file.write(str(num) + "NEW REVIEW")
    print("bezig")
    print('https://www.adidas.nl/api/models/IUU93/reviews?bazaarVoiceLocale=nl_NL&includeLocales=nl%2A&limit=10&offset=' + str(num) + '&sort=newest')
    response = client.get('https://www.adidas.nl/api/models/IUU93/reviews?bazaarVoiceLocale=nl_NL&includeLocales=nl%2A&limit=10&offset=' + str(num) + '&sort=newest',
                          params={
                              "render_js": "false"
    }
    )
    file.write(response.content.decode("utf-8").encode('cp850', 'replace').decode('cp850'))
    

file.close()
# output = str(response.content, 'UTF-8')


client1.write("/data/HM_Reviews1.txt", response.content)

