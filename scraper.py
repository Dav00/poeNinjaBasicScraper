from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class PriceDTO:
    def __init__(self, name, buy, sell):
        self.name = name
        self.buy = buy
        self.sell = sell
    def __str__(self):
        return f"{self.name}, {self.buy}, {self.sell}"
    
websiteCurrency = 'https://poe.ninja/challenge/currency'
path = 'chromedriver'
maxItems = 10

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
driver.get(websiteCurrency)
resultList = []
matches = driver.find_elements_by_tag_name('tr')


for n in range(len(matches)):
    if(n >= 2):
     match = matches[n]
     #print('Line: ' , n)
     fields = match.text.split("\n")
     resultList.append(PriceDTO(fields[0], fields[1], fields[2]))
    if(n == maxItems):
        break
for n in resultList:
    print(n)


