import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# Chrome setup (adjust path to your chromedriver if needed)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(executable_path="/Users/akshatpeter/Downloads/odisha_rera_scraper/chromedriver") 
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://rera.odisha.gov.in/projects/project-list")
time.sleep(5)

# Click "View Details" for first 6 projects
projects_data = []

for i in range(1, 7):
    try:
        view_button = driver.find_element(By.XPATH, f"(//a[contains(text(),'View Details')])[{i}]")
        view_button.click()
        time.sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        # Scrape required fields
        rera_no = soup.find("div", class_="rera_regd").text.strip().split(":")[-1].strip()
        project_name = soup.find("h4").text.strip()

        tabs = soup.find_all("div", class_="tab-pane")
        promoter_section = tabs[1] if len(tabs) > 1 else None

        promoter_name = promoter_section.find(text="Company Name").find_next().text.strip()
        promoter_address = promoter_section.find(text="Registered Office Address").find_next().text.strip()
        gst_no = promoter_section.find(text="GST No.").find_next().text.strip()

        projects_data.append({
            "Rera Regd. No": rera_no,
            "Project Name": project_name,
            "Promoter Name": promoter_name,
            "Promoter Address": promoter_address,
            "GST No": gst_no
        })

        driver.back()
        time.sleep(3)
    except Exception as e:
        print(f"Error scraping project {i}: {e}")

driver.quit()

df = pd.DataFrame(projects_data)
df.to_csv("odisha_rera_projects.csv", index=False)
print(" Data saved to 'odisha_rera_projects.csv'")

