import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def flipkart(product_name):
    product_info_list = []
    try:
        # URL of Flipkart
        querry = product_name.replace(' ', '+')
        web = f'https://www.flipkart.com/search?q={querry}'

        # Initialize a Chrome WebDriver
        driver = webdriver.Chrome()
        driver.get(web)

        # Parse the HTML source using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all product containers
        product_containers = soup.find_all("div", class_="_2kHMtA")

        # Initialize a list to store product information
     

        # Loop through product containers and extract information for each product
        for product_container in product_containers:
            product_name_element = product_container.select_one('a._1fQZEK')
            product_link_element = product_container.find('a', class_='_1fQZEK')
            product_price_element = product_container.find('div', class_='_30jeq3')

            if product_name_element and product_link_element and product_price_element:
                product_name = product_name_element.get_text()
                product_link = 'https://www.flipkart.com' + product_link_element['href']
                product_price = product_price_element.get_text()

                # Create a dictionary to store the information for the current product
                product_info = {
                "product_name": "Flpicart  -" + product_name,
                "product_price": product_price,
                "product_link": product_link
                }

                # Append the product information to the list
                product_info_list.append(product_info)
            
        # Close the browser
        driver.quit()
        return product_info_list 
    except Exception as e:
        return product_info_list
# Print the extracted information for each product
    


def amazone(product_name):
    web = 'https://www.amazon.in'

    # Initialize a Chrome WebDriver
    driver = webdriver.Chrome()
    driver.get(web)

    # Find the search bar element by ID and enter your search query
    search_query = product_name
    search_bar = driver.find_element(By.ID, 'twotabsearchtextbox')
    search_bar.send_keys(search_query)

    # Find the search button element by ID and click it
    search_button = driver.find_element(By.ID, 'nav-search-submit-button')
    search_button.click()

    # Wait for the page to load and get the page source
    time.sleep(5)
    html_source = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the HTML source using BeautifulSoup
    soup = BeautifulSoup(html_source, 'html.parser')

    # Find all product containers
    product_containers = soup.find_all("div", class_="s-result-item")

    # Initialize a list to store product information
    product_info_list = []

    # Loop through product containers and extract information for each product
    for product_container in product_containers:
        product_name_element = product_container.select_one('h2 a span')
        product_price_element = product_container.select_one('.a-price .a-offscreen')
        product_link_element = product_container.find("a", class_="a-link-normal")

        if product_name_element and product_price_element and product_link_element:
            product_name = product_name_element.get_text()
            product_price = product_price_element.get_text()
            product_link = "https://www.amazon.in" + product_link_element['href']

            # Create a dictionary to store the information for the current product
            product_info = {
                "product_name": "Amazone  -" + product_name,
                "product_price": product_price,
                "product_link": product_link
            }

            # Append the product information to the list
            product_info_list.append(product_info)

            return product_info_list


def shopclues(product_name):
    results = []
    try:
        # Define the URL for Shopclues search based on the provided product name
        search_url = f"https://www.shopclues.com/search?q={product_name.replace(' ', '+')}"

        # Send an HTTP GET request to the search URL
        response = requests.get(search_url)
     

        # Initialize an empty list to store the results
        

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all elements with the "prod_name" class (product name)
            product_names = soup.find_all("span", class_="prod_name")

            # Find all elements with the "p_price" class (product price)
            product_prices = soup.find_all(class_="p_price")

            # Find all elements with the "column col3" class
            product_link_containers = soup.find_all("div", class_="column col3")

            # Extract and store the product names, prices, and links in the results list
            for name, price, link_container in zip(product_names, product_prices, product_link_containers):
                product_name = name.get_text(strip=True)
                product_price = price.get_text(strip=True)
                
                # Find the product link with target="_blank"
                product_link = link_container.find("a", {"target": "_blank"})
                
                if product_link:
                    product_href = product_link['href']
                    
                    # Append the product details to the results list as a dictionary
                    results.append({
                        "product_name": "Shopclus  -" + product_name,
                        "product_price": product_price,
                        "product_link": product_href
                    })
            return results
    except Exception as e:
        return results

def snapdeal(product_name):
    results = []
    try:
        # Define the URL for Snapdeal search based on the provided product name
        search_url = f"https://www.snapdeal.com/search?keyword={product_name.replace(' ', '+')}&sort=rlvncy"

        # Send an HTTP GET request to the search URL
        response = requests.get(search_url)
        # Initialize an empty list to store the results
        

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all elements with the "product-title" class
            product_titles = soup.find_all(class_="product-title")

            # Find all elements with the "lfloat product-price" class
            product_prices = soup.find_all(class_="lfloat product-price")

            # Find all elements with the "dp-widget-link noUdLine" class
            product_links = soup.find_all(class_="dp-widget-link noUdLine")
            # Extract and store the product names, prices, and links in the results list
            for title, price, link in zip(product_titles, product_prices, product_links):
                product_name = title.get_text(strip=True)
                product_price = price.get_text(strip=True)
                product_href = link['href']

                if product_href:
                # Append the product details to the results list as a dictionary
                    results.append({
                        "product_name": "Snapdeal  -"+ product_name,
                        "product_price": product_price,
                        "product_link": product_href
                  })
            return results
    except Exception as e:
        return results
    
def scrape_myntra(product_name):
    # Initialize a Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to the URL
    url = f"https://www.myntra.com/{product_name.replace(' ', '+')}"
    driver.get(url)

    # Define the number of scrolls
    total_scrolls = 5

    # Function to scroll to the end of the page
    def scroll_to_end():
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Add a delay to allow content to load

    # Scroll to the middle of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
    time.sleep(2)  # Add a delay to allow content to load

    # Scroll the specified number of times
    for _ in range(total_scrolls - 1):
        scroll_to_end()

    # Get the page source (HTML content)
    page_source = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the page source using Beautiful Soup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find product names, prices, h4 tag text, and href links
    product_names = soup.find_all('h3', class_='product-brand')
    product_prices = soup.find_all('span', class_='product-discountedPrice')
    h4_texts = soup.find_all('h4', class_='product-product')
    product_links = soup.find_all('a', {'data-refreshpage': 'true', 'target': '_blank'})

    # Create a list to store the results
    results = []

    for name, price, h4_text, link in zip(product_names, product_prices, h4_texts, product_links):
        product_name = name.text.strip()
        product_price = price.text.strip()
        h4_text = h4_text.text.strip()
        combined_text = f"{product_name} {h4_text}"
        product_link = "https://myntra.com/" + link['href']

        # Append the product details to the results list as a dictionary
        results.append({
            "product_name": "Myntra  -" + combined_text,
            "product_price": product_price,
            "product_link": product_link
        })

    return results

def indiamart_scrap(product_name):
    # Initialize a Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to the URL
    url = f"https://dir.indiamart.com/search.mp?ss={product_name.replace(' ', '+')}"  # Replace with the actual URL
    driver.get(url)

    # Define the number of scrolls (you can adjust this as needed)
    total_scrolls = 5

    # Function to scroll to the end of the page
    def scroll_to_end():
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Add a delay to allow content to load

    # Scroll to the middle of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
    time.sleep(2)  # Add a delay to allow content to load

    # Scroll the specified number of times
    for _ in range(total_scrolls - 1):
        scroll_to_end()

    # Get the page source (HTML content)
    page_source = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the page source using Beautiful Soup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract product data
    product_data = []

    # Find the HTML elements containing product name and link
    name_and_link_elements = soup.find_all('span', {'class': 'elps elps2 p10b0 fs14 tac mListNme', 'data-click': '^Prod0Name'})

    # Find the HTML elements containing product price
    price_elements = soup.find_all('span', {'class': 'prc clr3 fwb fs18 cp'})

    for name_element, price_element in zip(name_and_link_elements, price_elements):
        product_name_element = name_element.find('a', class_='prd-name')
        product_name = product_name_element.text.strip() if product_name_element else ''
        
        product_link = product_name_element['href'] if product_name_element else ''
        
        product_price = price_element.text.strip() if price_element else ''
        
        # Check if any of the three pieces of information is missing
        if product_name and product_link and product_price:
            # product_data.append((product_name, product_link, product_price))
            product_data.append({
            "product_name": "Indiamart  -" + product_name,
            "product_price": product_price,
            "product_link": product_link
        })

    return product_data

def scrap(product_name):
    result1, result2, result3, result4, result5,result6 = [], [], [], [], [], []

    

    try:
        result1 = snapdeal(product_name)
        print("spanpdeal", len(result1))
    except Exception as e1:
        print(f"An error occurred while calling snapdeal: {e1}")

    try:
        result2 = shopclues(product_name)
        print("shopclues",len(result2))
    except Exception as e2:
        print(f"An error occurred while calling shopclues: {e2}")

    try:
        result3 = scrape_myntra(product_name)
        print("myntra",len(result3))
    except Exception as e3:
        print(f"An error occurred while calling scrape_myntra: {e3}")

    try:
        result4 = indiamart_scrap(product_name)
        print("Indiamart",len(result4))
    except Exception as e4:
        print(f"An error occurred while calling indiamart_scrap: {e4}")

    try:
        result5 = amazone(product_name)
        print("Amazone", len(result5))
    except Exception as e5:
        print(f"An error occurred while calling amazone_scrap: {e5}")

    try:
        result6 = flipkart(product_name)
    except Exception as e6:
        print(f"An error occurred while calling flipkart: {e6}")

    

    combined_list = []

    lists = [result1,result2,result3,result4,result5,result6]

    # Create a list of non-empty result lists
    non_empty_lists = [lst for lst in lists if lst is not None]

    # Check if there are non-empty lists
    if non_empty_lists:
        # Find the length of the longest non-empty list
        max_len = max(len(lst) for lst in non_empty_lists)

        for i in range(max_len):
            for lst in non_empty_lists:
                if i < len(lst):
                    combined_list.append(lst[i])


    return combined_list






