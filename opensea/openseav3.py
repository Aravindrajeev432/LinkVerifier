from selenium import webdriver



website = "https://opensea.io/rankings?sortBy=total_volume"
path = "/Users/arvindr/Downloads/chrome-mac-arm64/Google Chrome for Testing.app"

driver = webdriver.Chrome()
driver.get(website)
collection_links = driver.find_elements_by_xpath("//a[starts-with(@href, '/collection/')]")

# Extract and print the href attributes
for link in collection_links:
    print(link.get_attribute("href"))

# Close the browser window
driver.quit()