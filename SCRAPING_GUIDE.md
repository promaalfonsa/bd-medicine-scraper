# Medicine Scraper - CSV Export Guide

## Overview
This project scrapes medicine data from medex.com.bd and exports it to CSV files in the `Scraped` folder.

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
Create a `.env` file with the following:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
```

### 3. Database Setup
```bash
python manage.py migrate
```

## Running the Scraper

### Method 1: Using the Automated Script (Recommended)
Simply run the automated script which handles all scraping and export:
```bash
python scrape_and_export.py
```

This script will:
1. Scrape manufacturers from medex.com.bd
2. Scrape generic medicines information
3. Scrape all medicine brands
4. Export the data to `Scraped/medicines_list.csv`

### Method 2: Manual Step-by-Step
If you prefer to run each step manually:

1. Scrape manufacturers:
```bash
python manage.py manufacturer_crawl
```

2. Scrape generics:
```bash
python manage.py generic_crawl
```

3. Scrape medicines:
```bash
python manage.py med_crawl
```

4. Export to CSV:
```bash
python manage.py export_medicines_csv
```

## CSV Output Format

The exported CSV file (`Scraped/medicines_list.csv`) contains three columns:

| Column Name | Description |
|------------|-------------|
| Name of the Medicine | Brand name of the medicine |
| Type of the Medicine | Either "Allopathic" or "Herbal" |
| Usage of the Medicine | Description of what the medicine is used for (from generic indication) |

## Example Output

```csv
Name of the Medicine,Type of the Medicine,Usage of the Medicine
Napa,Allopathic,"Paracetamol is used for the relief of mild to moderate pain and reduction of fever..."
Amdocal,Allopathic,"Amlodipine is used to treat high blood pressure (hypertension) and chest pain..."
```

## Troubleshooting

### Network Access Issues
The scraper requires internet access to medex.com.bd. If you're in a restricted environment:
- Ensure the website is accessible
- Check if you need to configure proxy settings in `.env`

### Scraped Folder Location
The CSV file is saved to: `./Scraped/medicines_list.csv`

### Database Issues
If you encounter database errors, try:
```bash
python manage.py migrate --run-syncdb
```

## Notes

- The scraper respects robots.txt and includes delays between requests
- All scraped data is stored in the SQLite database (db.sqlite3)
- The `Scraped` folder is automatically created if it doesn't exist
- You can re-run the export command anytime to regenerate the CSV from the database
