from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from django.contrib.auth.models import User
from blog import models

#  each class below should have a name that ends with `Type`
#  because each reps a GraphQL type

class UserType(DjangoObjectType):
    class Meta:
        model = User

class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile

class PostType(DjangoObjectType):
    class Meta:
        model = models.Post

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag

"""
Bring together all classes above add methods to it and indicate how models can 
be queried
"""

class Query(graphene.ObjectType):

    all_posts = graphene.List(PostType)
    author_by_username = graphene.Field(AuthorType, username=graphene.String())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    posts_by_author = graphene.List(PostType, username=graphene.String())
    posts_by_tag = graphene.List(PostType, tag=graphene.String())

    def resolve_all_posts(root, info):
        return(
            models.Post.objects.prefetch_related("tags").select_related("author").all()
        )

    def resolve_author_by_username(root, info, username):
        return (models.Profile.objects.select_related("user").get(user__username=username))

    def resolve_posts_by_author(root, info, username):
        return ( models.Post.objects.prefetch_related("tags").select_related("author").filter(author__user__username=username))

    def resolve_posts_by_tag(root, info, tag):
        return (models.Post.objects.prefetch_related("tags").select_related("author").filter(tags__name__iexact=tag))

# schema = graphene.Schema(query=Query)

schema = graphene.Schema(query=Query)









