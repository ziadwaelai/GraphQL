from django.db import models

class KPI(models.Model):
    name = models.CharField(max_length=100)
    expression = models.TextField()  # Stores the equation for the KPI
    description = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.name

class AssetKPI(models.Model):
    asset_id = models.CharField(max_length=100)
    kpi = models.ForeignKey(KPI, on_delete=models.CASCADE, related_name="assets")
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.TextField()  # Stores the output value after processing

    def __str__(self):
        return f"{self.asset_id} - {self.kpi.name}"
