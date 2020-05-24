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