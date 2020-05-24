import graphene

import games.schema
import users.schema


class Query(
    users.schema.Query,
    games.schema.Query,
    graphene.ObjectType):
    pass

class Mutation(
    games.schema.Mutation,
    users.schema.Mutation,
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
