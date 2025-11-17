#!/usr/bin/env python
"""
Script to scrape medicine data and export to CSV

This script will:
1. Run the medicine crawler to scrape data from medex.com.bd
2. Export the scraped data to CSV in the Scraped folder

Note: The scraper requires internet access to medex.com.bd
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.core.management import call_command


def main():
    print("=" * 60)
    print("BD Medicine Scraper - Data Collection and Export")
    print("=" * 60)
    print()
    
    # Step 1: Run manufacturer crawler
    print("Step 1: Scraping manufacturers...")
    try:
        call_command('manufacturer_crawl')
        print("✓ Manufacturers scraped successfully")
    except Exception as e:
        print(f"⚠ Warning: Manufacturer scraping encountered an issue: {e}")
    
    print()
    
    # Step 2: Run generic crawler
    print("Step 2: Scraping generics...")
    try:
        call_command('generic_crawl')
        print("✓ Generics scraped successfully")
    except Exception as e:
        print(f"⚠ Warning: Generic scraping encountered an issue: {e}")
    
    print()
    
    # Step 3: Run medicine crawler
    print("Step 3: Scraping medicines...")
    try:
        call_command('med_crawl')
        print("✓ Medicines scraped successfully")
    except Exception as e:
        print(f"⚠ Warning: Medicine scraping encountered an issue: {e}")
    
    print()
    
    # Step 4: Export to CSV
    print("Step 4: Exporting data to CSV...")
    try:
        call_command('export_medicines_csv')
        print("✓ Data exported successfully to Scraped/medicines_list.csv")
    except Exception as e:
        print(f"✗ Error: Failed to export data: {e}")
        return 1
    
    print()
    print("=" * 60)
    print("Process completed!")
    print("Check the 'Scraped' folder for the CSV file.")
    print("=" * 60)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
