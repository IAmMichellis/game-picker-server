import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from .models import Game
from users.schema import UserType
from django.db.models import Q


class GameType(DjangoObjectType):
    class Meta:
        model = Game


class Query(graphene.ObjectType):
    games = graphene.List(GameType, search=graphene.String())

    def resolve_games(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(title__icontains=search)
            )
            return Game.objects.filter(filter)

        return Game.objects.all()

class CreateGame(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    created_by = graphene.Field(UserType)


    class Arguments:
        title = graphene.String()

    def mutate(self, info, title):
        user = info.context.user or None
        if user.is_anonymous:
            raise GraphQLError('You must be logged to vote!')

        game = Game(
            title=title,
            created_by=user
        )
        game.save()

        return CreateGame(
            id=game.id,
            title=game.title,
            created_by=game.posted_by,
        )

class Mutation(graphene.ObjectType):
    create_game = CreateGame.Field()