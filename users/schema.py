import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from users.models import Roles
from reserves.models import Users

class UserType(DjangoObjectType):
    class Meta:
        model = Users 
        fields = "__all__"

class RoleType(DjangoObjectType):
    class Meta:
        model = Roles 
        fields = "__all__"

class Query(graphene.ObjectType):
    all_user = graphene.List(UserType)
    all_role = graphene.List(RoleType)
    
    @login_required
    def resolve_all_user(root, info):
        return Users.objects.all()
    
    @login_required
    def resolve_all_role(root, info):
        return Roles.objects.all()


#Mutations
class RoleInput(graphene.InputObjectType):
    name = graphene.String()

class Role(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    insertAt = graphene.DateTime()

class CreateRole(graphene.Mutation):
    role = graphene.Field(lambda: Role)

    class Arguments:
        input = RoleInput() 

    @login_required
    def mutate(self, info, input):
        role = Roles(
                name=input.name
                )
        role.save()
        return CreateRole(role=role)

class Mutation(graphene.ObjectType):
    create_role = CreateRole.Field()
