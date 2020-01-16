import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from ckeckers_api.models import Game


# Create a GraphQL type for the actor model
class GameType(DjangoObjectType):
    class Meta:
        model = Game
# Create a GraphQL type for the movie model
# class MovieType(DjangoObjectType):
#     class Meta:
#         model = Movie

class Query(ObjectType):
    # actor = graphene.Field(ActorType, id=graphene.Int())
    # movie = graphene.Field(MovieType, id=graphene.Int())

    game = graphene.Field(GameType, id=graphene.Int())

    # actors = graphene.List(ActorType)
    # movies = graphene.List(MovieType)

    movies = graphene.List(GameType)

    def resolve_game(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Game.objects.get(pk=id)
        return None

    # def resolve_actor(self, info, **kwargs):
    #     id = kwargs.get('id')
    #     if id is not None:
    #         return Actor.objects.get(pk=id)
    #     return None
    # def resolve_movie(self, info, **kwargs):
    #     id = kwargs.get('id')
    #     if id is not None:
    #         return Movie.objects.get(pk=id)
    #     return None
    # def resolve_actors(self, info, **kwargs):
    #     return Actor.objects.all()
    # def resolve_movies(self, info, **kwargs):
    #     return Movie.objects.all()

    def resolve_games(self, info, **kwargs):
        return Game.objects.all()

