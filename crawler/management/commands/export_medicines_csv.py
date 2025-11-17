import csv
import os
from django.core.management import BaseCommand
from crawler.models import Medicine


class Command(BaseCommand):
    help = "Export medicines to CSV file with Name, Type, and Usage columns in Scraped folder"

    def handle(self, *args, **options):
        # Create Scraped folder if it doesn't exist
        output_dir = "Scraped"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        output_file = os.path.join(output_dir, "medicines_list.csv")
        
        self.stdout.write(f"Exporting medicines to {output_file}...")
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write header
            writer.writerow(['Name of the Medicine', 'Type of the Medicine', 'Usage of the Medicine'])
            
            # Write data rows
            count = 0
            for medicine in Medicine.objects.select_related('generic', 'generic__indication').all():
                name = medicine.brand_name or ''
                med_type = medicine.get_type_display() if medicine.type else medicine.type or ''
                
                # Get usage from generic's indication description
                usage = ''
                if medicine.generic and medicine.generic.indication_description:
                    usage = medicine.generic.indication_description.strip()
                
                writer.writerow([name, med_type, usage])
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully exported {count} medicines to {output_file}'))
