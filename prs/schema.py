import graphene
import graphql_jwt
from graphene_django import DjangoObjectType

#Schemes
import users.schema
import catalogs.schema

class Query(users.schema.Query, catalogs.schema.Query):
    pass

class Mutation(users.schema.Mutation, catalogs.schema.Mutation):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
