# import requests
# from selenium import webdriver
# import time
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By


# # java
# # from selenium import webdriver
# # chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument("--no-sandbox")
# # chrome_options.add_argument("--headless")
# # chrome_options.add_argument("--disable-gpu")
# # driver = webdriver.Chrome(options=chrome_options)

# # # global driver

# def flipkart(product_name):
#     product_info_list = []
#     try:
#         # URL of Flipkart
#         querry = product_name.replace(' ', '+')
#         web = f'https://www.flipkart.com/search?q={querry}'

#         # Initialize a Chrome WebDriver
#         # driver = webdriver.Chrome()
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--disable-gpu")
#         chrome_options.add_argument('--disable-dev-shm-usage')
#         driver = webdriver.Chrome(options=chrome_options)
#         driver.get(web)

#         # Parse the HTML source using BeautifulSoup
#         soup = BeautifulSoup(driver.page_source, 'html.parser')

#         # Find all product containers
#         product_containers = soup.find_all("div", class_="_2kHMtA")

#         # Initialize a list to store product information


#         # Loop through product containers and extract information for each product
#         for product_container in product_containers:
#             product_name_element = product_container.select_one('a._1fQZEK')
#             product_link_element = product_container.find('a', class_='_1fQZEK')
#             product_price_element = product_container.find('div', class_='_30jeq3')

#             if product_name_element and product_link_element and product_price_element:
#                 product_name = product_name_element.get_text()
#                 product_link = 'https://www.flipkart.com' + product_link_element['href']
#                 product_price = product_price_element.get_text()

#                 # Create a dictionary to store the information for the current product
#                 product_info = {
#                 "product_name": "Flpicart  -" + product_name,
#                 "product_price": product_price,
#                 "product_link": product_link
#                 }

#                 # Append the product information to the list
#                 product_info_list.append(product_info)

#         # Close the browser
#         driver.quit()
#         return product_info_list
#     except Exception as e:
#         print(f"java -------------------------------- {e}")
#         return product_info_list

# def amazone(product_name):
#     try:

#         web = 'https://www.amazon.in'

#         # Initialize a Chrome WebDriver
#         # driver = webdriver.Chrome()
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--disable-gpu")
#         chrome_options.add_argument('--disable-dev-shm-usage')
#         driver = webdriver.Chrome(options=chrome_options)
#         driver.get(web)

#         # Find the search bar element by ID and enter your search query
#         search_query = product_name
#         search_bar = driver.find_element(By.ID, 'twotabsearchtextbox')
#         search_bar.send_keys(search_query)

#         # Find the search button element by ID and click it
#         search_button = driver.find_element(By.ID, 'nav-search-submit-button')
#         search_button.click()

#         # Wait for the page to load and get the page source
#         time.sleep(5)
#         html_source = driver.page_source


#         soup = BeautifulSoup(html_source, 'html.parser')

#         product_containers = soup.find_all("div", class_="s-result-item")

#         product_info_list = []

#         for product_container in product_containers:
#             product_name_element = product_container.select_one('h2 a span')
#             product_price_element = product_container.select_one('.a-price .a-offscreen')
#             product_link_element = product_container.find("a", class_="a-link-normal")

#             if product_name_element and product_price_element and product_link_element:
#                 product_name = product_name_element.get_text()
#                 product_price = product_price_element.get_text()
#                 product_link = "https://www.amazon.in" + product_link_element['href']

#                 product_info = {
#                     "product_name": "Amazone  -" + product_name,
#                     "product_price": product_price,
#                     "product_link": product_link
#                 }

#                 product_info_list.append(product_info)

#                 return product_info_list
#         driver.quit()
#     except Exception as e:
#         print(product_info_list)
#         return product_info_list



# def scrap(product_name):
#     try :

#         result1,result2 = [], []

#         result1 = amazone(product_name)
#         result2 = flipkart(product_name)

#         if result1:
#             print("Amazon",len(result1))
#         elif result2:
#             print("Flipkart",len(result2))
#         else:
#             print("None")

#     except Exception as e:
#         print(f"An error occurred : {e}")

#     combined_list = []

#     lists = [result1,result2]

#     non_empty_lists = [lst for lst in lists if lst is not None]

#     if non_empty_lists:
#         max_len = max(len(lst) for lst in non_empty_lists)

#         for i in range(max_len):
#             for lst in non_empty_lists:
#                 if i < len(lst):
#                     combined_list.append(lst[i])

#     return combined_list







from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def flipkart(product_name):
    try:
        product_info_list = []
        web = f'https://www.flipkart.com/search?q={product_name.replace(" ", "+")}'
        driver = webdriver.Chrome()  # Use default options for clarity
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        # driver = webdriver.Chrome(options=chrome_options)
        driver.get(web)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        product_containers = soup.find_all("div", class_="_2kHMtA")
        for product_container in product_containers:
            product_name_element = product_container.select_one('a._1fQZEK')
            product_link_element = product_container.find('a', class_='_1fQZEK')
            product_price_element = product_container.find('div', class_='_30jeq3')
            if product_name_element and product_link_element and product_price_element:
                product_name = product_name_element.get_text()
                product_link = 'https://www.flipkart.com' + product_link_element['href']
                product_price = product_price_element.get_text()
                product_info = {
                    "product_name": "Flipkart - " + product_name,  # Corrected typo
                    "product_price": product_price,
                    "product_link": product_link
                }
                product_info_list.append(product_info)
        driver.quit()
        return product_info_list
    except Exception as e :
        print(f"java ------------------------- {e}")
        
def amazone(product_name):
    try:
        web = 'https://www.amazon.in'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()  # Use default options for clarity
        driver.get(web)
        search_bar = driver.find_element(By.ID, 'twotabsearchtextbox')
        search_bar.send_keys(product_name)
        search_button = driver.find_element(By.ID, 'nav-search-submit-button')
        search_button.click()
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        product_containers = soup.find_all("div", class_="s-result-item")
        product_info_list = []
        for product_container in product_containers:
            product_name_element = product_container.select_one('h2 a span')
            product_price_element = product_container.select_one('.a-price .a-offscreen')
            product_link_element = product_container.find("a", class_="a-link-normal")
            if product_name_element and product_price_element and product_link_element:
                product_name = product_name_element.get_text()
                product_price = product_price_element.get_text()
                product_link = "https://www.amazon.in" + product_link_element['href']
                product_info = {
                    "product_name": "Amazon - " + product_name,  # Corrected typo
                    "product_price": product_price,
                    "product_link": product_link
                }
                product_info_list.append(product_info)
            else:
                print(f"Product element not found: {product_container}")  # Add logging for debugging
        return product_info_list
        driver.quit()  # Ensure driver is closed
    except Exception as e:
        print(f"java ------------------------- {e}")

def scrap(product_name):
    result1 = amazone(product_name)
    # result2 = flipkart(product_name)
    if result1:
        print(f"amazon ----------------- {result1}")
    # elif result2:
    #     print(f"amazon ----------------- {result2}")
    combined_list = []
    for lst in [result1]:
        if lst:
            combined_list.extend(lst)  # Combine lists efficiently
    return combined_list
