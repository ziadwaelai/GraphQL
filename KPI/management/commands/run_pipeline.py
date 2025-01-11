from django.core.management.base import BaseCommand
from KPI.services.pipeline import run_data_pipeline

class Command(BaseCommand):
    help = 'Run the data ingestion and processing pipeline'

    def add_arguments(self, parser):
        parser.add_argument('--file_path', type=str, required=True, help='Path to the messages file')
        parser.add_argument('--equation', type=str, required=True, help='Equation for processing')
        parser.add_argument('--kpi_id', type=int, required=True, help='KPI ID for storing results')

    def handle(self, *args, **options):
        file_path = options['file_path']
        equation = options['equation']
        kpi_id = options['kpi_id']
        
        run_data_pipeline(file_path, equation, kpi_id)
        self.stdout.write(self.style.SUCCESS("Data pipeline completed successfully"))
