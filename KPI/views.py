# from django.http import JsonResponse
# from KPI.services.context import Context

# def evaluate_expression_view(request):
#     expression_text = request.GET.get("expression")
#     if not expression_text:
#         return JsonResponse({"error": "No expression provided"}, status=400)

#     try:
#         context = Context(expression_text)
#         print(expression_text)
#         result = context.evaluate()
#         return JsonResponse({"result": result})
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from KPI.models import KPI, AssetKPI
from KPI.serializers import KPISerializer, AssetKPISerializer

class KPIViewSet(viewsets.ModelViewSet):
    queryset = KPI.objects.all()
    serializer_class = KPISerializer

    @action(detail=True, methods=['post'])
    def link_asset(self, request, pk=None):
        kpi = self.get_object()
        asset_id = request.data.get('asset_id')
        value = request.data.get('value')

        if not asset_id:
            return Response({"error": "Asset ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        asset_kpi = AssetKPI.objects.create(asset_id=asset_id, kpi=kpi, value=value)
        serializer = AssetKPISerializer(asset_kpi)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
