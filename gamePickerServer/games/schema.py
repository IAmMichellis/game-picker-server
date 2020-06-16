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
    games = graphene.List(
        GameType,
        search=graphene.String(),
        first=graphene.Int(),
        skip=graphene.Int(), 
        )

    def resolve_games(self, info, search=None, first=None, skip=None, **kwargs):
        games = Game.objects.all()

        if search:
            filter = (
                Q(title__icontains=search)
            )
            games = games.filter(filter)

        if skip:
            games = games[skip:]

        if first:
            games = games[:first]

        return games

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