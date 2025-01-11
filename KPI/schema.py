import graphene
from graphene_django.types import DjangoObjectType
from .models import KPI, AssetKPI


class KPIType(DjangoObjectType):
    class Meta:
        model = KPI
        fields = ('id', 'name', 'expression', 'description')


class AssetKPIType(DjangoObjectType):
    class Meta:
        model = AssetKPI
        fields = ('id', 'asset_id', 'kpi', 'timestamp', 'value')


class Query(graphene.ObjectType):
    all_kpis = graphene.List(KPIType)

    all_asset_kpis = graphene.List(AssetKPIType)

    def resolve_all_kpis(self, info, **kwargs):
        return KPI.objects.all()

    def resolve_all_asset_kpis(self, info, **kwargs):
        return AssetKPI.objects.all()


class CreateKPI(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        expression = graphene.String(required=True)
        description = graphene.String()

    kpi = graphene.Field(KPIType)

    def mutate(self, info, name, expression, description=None):
        kpi = KPI.objects.create(name=name, expression=expression, description=description)
        return CreateKPI(kpi=kpi)


class DeleteKPI(graphene.Mutation):
    class Arguments:
        kpi_id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, kpi_id):
        try:
            kpi = KPI.objects.get(pk=kpi_id)
            kpi.delete()
            return DeleteKPI(success=True)
        except KPI.DoesNotExist:
            raise Exception("KPI with the given ID does not exist")


class UpdateKPI(graphene.Mutation):
    class Arguments:
        kpi_id = graphene.Int(required=True)
        name = graphene.String()
        expression = graphene.String()
        description = graphene.String()

    kpi = graphene.Field(KPIType)

    def mutate(self, info, kpi_id, name=None, expression=None, description=None):
        try:
            kpi = KPI.objects.get(pk=kpi_id)
            if name:
                kpi.name = name
            if expression:
                kpi.expression = expression
            if description:
                kpi.description = description
            kpi.save()
            return UpdateKPI(kpi=kpi)
        except KPI.DoesNotExist:
            raise Exception("KPI with the given ID does not exist")


class LinkAssetToKPI(graphene.Mutation):
    class Arguments:
        asset_id = graphene.String(required=True)
        kpi_id = graphene.Int(required=True)
        value = graphene.String(required=True)

    asset_kpi = graphene.Field(AssetKPIType)

    def mutate(self, info, asset_id, kpi_id, value):
        try:
            kpi = KPI.objects.get(pk=kpi_id)
            asset_kpi = AssetKPI.objects.create(asset_id=asset_id, kpi=kpi, value=value)
            return LinkAssetToKPI(asset_kpi=asset_kpi)
        except KPI.DoesNotExist:
            raise Exception("KPI with the given ID does not exist")


# Combine all mutations
class Mutation(graphene.ObjectType):
    create_kpi = CreateKPI.Field()
    delete_kpi = DeleteKPI.Field()
    update_kpi = UpdateKPI.Field()
    link_asset_to_kpi = LinkAssetToKPI.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
