from rest_framework import serializers
from KPI.models import KPI, AssetKPI

class KPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = ['id', 'name', 'expression', 'description']

class AssetKPISerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetKPI
        fields = ['id', 'asset_id', 'kpi', 'timestamp', 'value']
