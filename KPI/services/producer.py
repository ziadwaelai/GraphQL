from datetime import datetime
from KPI.models import AssetKPI

class MessageProducer:
    def __init__(self, kpi):
        self.kpi = kpi

    def produce_message(self, asset_id, value):
        """Construct the message format and store it in the database."""
        message = {
            "asset_id": asset_id,
            "attribute_id": f"output_{self.kpi.id}",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "value": value
        }
        # Save to the database
        AssetKPI.objects.create(asset_id=asset_id, kpi=self.kpi, value=value)
        return message
