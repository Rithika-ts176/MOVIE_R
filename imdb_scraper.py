from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def init_browser():
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def scrape_imdb_top250():
    driver = init_browser()
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    # NEW IMDb structure: list items inside <ul>
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.ipc-metadata-list li")))

    movies = driver.find_elements(By.CSS_SELECTOR, "ul.ipc-metadata-list li")

    data = []

    for movie in movies:
        try:
            title = movie.find_element(By.CSS_SELECTOR, "h3").text
            rating = movie.find_element(By.CSS_SELECTOR, ".ipc-rating-star--rating").text
            year = movie.find_element(By.CSS_SELECTOR, ".cli-title-metadata span:nth-child(1)").text
            rank = title.split(".")[0]
            
            data.append({
                "Rank": rank,
                "Title": title.replace(rank + ". ", ""),
                "Year": year,
                "Rating": rating
            })
        except:
            continue

    driver.quit()

    df = pd.DataFrame(data)
    df.to_csv("imdb_top250.csv", index=False)
    
    print("✔ Scraping completed successfully!")
    print("✔ File saved as imdb_top250.csv")


if __name__ == "__main__":
    scrape_imdb_top250()
