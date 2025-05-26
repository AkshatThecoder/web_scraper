# Odisha RERA Project Scraper

Scrapes the first 6 "Projects Registered" from the Odisha RERA portal.

## 🔗 Target Site
https://rera.odisha.gov.in/projects/project-list

## Features
- Extracts RERA Regd. No, Project Name, Promoter Name, Promoter Address, GST No
- Headless browser automation using Selenium
- Data saved to CSV

## Requirements
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Output
- `odisha_rera_projects.csv`

## Notes
- Ensure ChromeDriver is installed and available in system PATH.
