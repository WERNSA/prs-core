import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from catalogs.models import Regions, Cities, Routes

class RegionType(DjangoObjectType):
    class Meta:
        model = Regions 
        fields = "__all__"

class CitiesType(DjangoObjectType):
    class Meta:
        model = Cities 
        fields = "__all__"

class Query(graphene.ObjectType):
    all_region = graphene.List(RegionType)
    all_cities = graphene.List(RegionType)
    
    @login_required
    def resolve_all_region(root, info):
        return Regions.objects.all()
    
    @login_required
    def resolve_all_cities(root, info):
        return Cities.objects.all()

#Mutations
class RegionInput(graphene.InputObjectType):
    name = graphene.String()
    iso = graphene.String()

class CitieInput(graphene.InputObjectType):
    name = graphene.String()
    regionId = graphene.Int()

class Region(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    iso = graphene.String()

class Citie(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    regionId = graphene.Int()

class CreateRegion(graphene.Mutation):
    region = graphene.Field(lambda: Region)

    class Arguments:
        input = RegionInput() 

    @login_required
    def mutate(self, info, input):
        region = Regions(
                name=input.name,
                iso=input.iso
                )
        region.save()
        return CreateRegion(region=region)

class CreateCitie(graphene.Mutation):
    citie = graphene.Field(lambda: Citie)

    class Arguments:
        input = CitieInput() 

    @login_required
    def mutate(self, info, input):
        citie = Cities(
                name=input.name,
                regions=input.regionId
                )
        citie.save()
        return CreateCitie(citie=citie)

class Mutation(graphene.ObjectType):
    create_region = CreateRegion.Field()
    create_citie = CreateCitie.Field()
