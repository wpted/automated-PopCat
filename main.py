from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Get user input
user_click = int(input("How many times do you want to pop the cat? Help rank-up your country! "))

# Initialize driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Access the given url and pop the cat
popcat_url = "https://popcat.click/"
driver.get(url=popcat_url)
cat_img = driver.find_element(By.CLASS_NAME, "cat-img")

# Pop the cat then stop the program
count = 0
while count <= user_click:
    cat_img.click()
    count += 1

driver.quit()
