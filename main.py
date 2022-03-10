from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

popcat_url = "https://popcat.click/"
driver.get(url=popcat_url)

cat_img = driver.find_element(By.CLASS_NAME, "cat-img")

count = 0

while count <= 100:

    cat_img.click()
    count += 1

# driver.quit()


