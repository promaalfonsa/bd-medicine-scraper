# Medicine Scraper - Quick Start Guide

## What This Does
This project scrapes medicine information from medex.com.bd and exports it to a CSV file containing:
- **Name of the Medicine** - The brand name (e.g., "Napa", "Amdocal")
- **Type of the Medicine** - Either "Allopathic" or "Herbal"
- **Usage of the Medicine** - What the medicine is used for

## Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install Django==3.2.12 djangorestframework==3.12.2 scrapy scrapy-djangoitem python-dotenv django-filter==21.1 django-admin-autocomplete-filter==0.7.1
```

### Step 2: Setup Database
```bash
python manage.py migrate
```

### Step 3: Run Scraper and Export
```bash
python scrape_and_export.py
```

The CSV file will be saved to: **`Scraped/medicines_list.csv`**

## Alternative: Export Existing Data Only

If you already have medicine data in your database and just want to export it:

```bash
python manage.py export_medicines_csv
```

## Example CSV Output

```csv
Name of the Medicine,Type of the Medicine,Usage of the Medicine
Napa,Allopathic,"Paracetamol is used for the relief of mild to moderate pain..."
Amdocal,Allopathic,"Amlodipine is used to treat high blood pressure..."
Herbal Napa,Herbal,"Paracetamol is used for the relief of mild to moderate pain..."
```

## What Gets Scraped

The scraper collects:
1. **Manufacturers** - Medicine companies
2. **Generics** - Generic medicine information with usage/indications
3. **Medicines** - Brand medicines with their generic associations

## File Locations

- **Output CSV**: `Scraped/medicines_list.csv`
- **Database**: `db.sqlite3` (SQLite database)
- **Export Command**: `crawler/management/commands/export_medicines_csv.py`
- **Automated Script**: `scrape_and_export.py`

## Troubleshooting

### "No medicines found in database"
Run the scraper first:
```bash
python scrape_and_export.py
```

### "Network error" or "DNS lookup failed"
The website medex.com.bd may be:
- Temporarily down
- Blocked in your region
- Requires proxy configuration

### Need more details?
See [SCRAPING_GUIDE.md](SCRAPING_GUIDE.md) for complete documentation.

## Technical Details

- **Framework**: Django + Scrapy
- **Database**: SQLite (default) or PostgreSQL
- **Export Format**: CSV with UTF-8 encoding
- **Data Source**: https://medex.com.bd

---

**Note**: The scraper respects the website's robots.txt and includes a 0.25 second delay between requests to be polite to the server.
