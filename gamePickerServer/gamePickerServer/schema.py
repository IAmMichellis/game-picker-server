import graphene

import games.schema


class Query(games.schema.Query, graphene.ObjectType):
    pass

class Mutation(games.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
