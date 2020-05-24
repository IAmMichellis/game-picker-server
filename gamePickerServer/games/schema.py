import graphene
from graphene_django import DjangoObjectType

from .models import Game


class GameType(DjangoObjectType):
    class Meta:
        model = Game


class Query(graphene.ObjectType):
    games = graphene.List(GameType)

    def resolve_games(self, info, **kwargs):
        return Game.objects.all()

class CreateGame(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()

    class Arguments:
        title = graphene.String()

    def mutate(self, info, title):
        game = Game(title=title)
        game.save()

        return CreateGame(
            id=game.id,
            title=game.title,
        )

class Mutation(graphene.ObjectType):
    create_game = CreateGame.Field()