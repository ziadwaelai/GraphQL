from KPI.services.ingestor import DataIngestor
from KPI.services.processing_engine import ProcessingEngine
from KPI.services.producer import MessageProducer
from KPI.models import KPI

def run_data_pipeline(file_path, equation, kpi_id):
    ingestor = DataIngestor(file_path)
    processing_engine = ProcessingEngine(equation)
    kpi = KPI.objects.get(id=kpi_id)
    producer = MessageProducer(kpi)

    for message in ingestor.read_messages():
        processed_value = processing_engine.process(message)
        result = producer.produce_message(message["asset_id"], processed_value)
        print("Processed Message:", result)
